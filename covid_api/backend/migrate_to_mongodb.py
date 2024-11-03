import psycopg2
from pymongo import MongoClient
from config import settings
import sys

def connect_to_postgres():
    try:
        # Conectar a PostgreSQL usando el usuario actual del sistema
        conn = psycopg2.connect(
            dbname="covid_db",
            user=sys.argv[1] if len(sys.argv) > 1 else None,
            host="localhost"
        )
        print("Successfully connected to PostgreSQL")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def connect_to_mongodb():
    try:
        client = MongoClient(settings.DATABASE_URL)
        db = client[settings.DATABASE_NAME]
        # Verificar la conexión
        client.server_info()
        print("Successfully connected to MongoDB")
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def migrate_covid_data():
    # Conectar a PostgreSQL
    pg_conn = connect_to_postgres()
    if pg_conn is None:
        print("Failed to connect to PostgreSQL")
        return

    # Conectar a MongoDB
    mongo_db = connect_to_mongodb()
    if mongo_db is None:
        print("Failed to connect to MongoDB")
        if pg_conn:
            pg_conn.close()
        return

    try:
        cursor = pg_conn.cursor()
        
        # Verificar si la tabla existe
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'covid_data'
            );
        """)
        
        if not cursor.fetchone()[0]:
            print("Table 'covid_data' does not exist in PostgreSQL")
            return

        # Obtener datos de PostgreSQL
        print("Fetching data from PostgreSQL...")
        cursor.execute("""
            SELECT 
                country,
                date_reported,
                country_code,
                who_region,
                new_cases,
                cumulative_cases,
                new_deaths,
                cumulative_deaths
            FROM covid_data
        """)
        
        # Procesar los resultados
        batch_size = 1000
        batch = []
        total_migrated = 0
        
        print("Starting migration...")
        for row in cursor:
            document = {
                "country": row[0],
                "date_reported": row[1].isoformat() if row[1] else None,
                "country_code": row[2],
                "who_region": row[3],
                "new_cases": int(row[4]) if row[4] is not None else 0,
                "cumulative_cases": int(row[5]) if row[5] is not None else 0,
                "new_deaths": int(row[6]) if row[6] is not None else 0,
                "cumulative_deaths": int(row[7]) if row[7] is not None else 0
            }
            batch.append(document)
            
            if len(batch) >= batch_size:
                mongo_db.covid_data.insert_many(batch)
                total_migrated += len(batch)
                print(f"Migrated {total_migrated} records")
                batch = []
        
        # Insertar registros restantes
        if batch:
            mongo_db.covid_data.insert_many(batch)
            total_migrated += len(batch)
            print(f"Migrated {total_migrated} records")
        
        # Crear índices
        print("Creating indexes...")
        mongo_db.covid_data.create_index("country")
        mongo_db.covid_data.create_index("date_reported")
        
        print("Migration completed successfully")
        
    except Exception as e:
        print(f"Error during migration: {e}")
    finally:
        cursor.close()
        pg_conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python migrate_to_mongodb.py <postgres_username>")
        sys.exit(1)
    
    migrate_covid_data()