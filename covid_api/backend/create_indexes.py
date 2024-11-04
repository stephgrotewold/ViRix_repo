from pymongo import MongoClient, ASCENDING
from config import settings

def setup_indexes():
    client = MongoClient(settings.DATABASE_URL)
    db = client[settings.DATABASE_NAME]
    
    try:
        # Eliminar índices existentes excepto _id_
        existing_indexes = list(db.health_centers.list_indexes())
        for index in existing_indexes:
            if index['name'] != '_id_':
                db.health_centers.drop_index(index['name'])
        
        print("Índices anteriores eliminados")
        
        # Crear nuevos índices
        db.health_centers.create_index(
            [("latitude", ASCENDING), ("longitude", ASCENDING)],
            name="location_index"
        )
        db.health_centers.create_index(
            [("services", ASCENDING)],
            name="services_index"
        )
        
        print("Nuevos índices creados:")
        for index in db.health_centers.list_indexes():
            print(f"- {index['name']}")
            
    except Exception as e:
        print(f"Error al configurar índices: {e}")

if __name__ == "__main__":
    setup_indexes()