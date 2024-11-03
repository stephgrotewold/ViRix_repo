# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


from pymongo import MongoClient
from config import settings

client = MongoClient(settings.DATABASE_URL)
db = client[settings.DATABASE_NAME]





# # URL de la base de datos (reemplaza <your_password> si es necesario)
# DATABASE_URL = "postgresql://stephgrotewold:<your_password>@localhost/covid_db"

# engine = create_engine(
#     DATABASE_URL,
#     echo=True,  # Activa el modo de depuración para ver las consultas SQL en la consola
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # Dependencia para obtener una sesión de la base de datos
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()