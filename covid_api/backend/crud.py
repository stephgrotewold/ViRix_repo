# from repositories import HealthCenterRepository, CovidDataRepository


from typing import Optional, List
from pymongo.collection import Collection
from bson import ObjectId
from repositories import HealthCenterRepository, CovidDataRepository, HealthCenter
import schemas
from pymongo.database import Database
from models import HealthCenter, CovidData
from config import get_collection, get_database
from database import db
from schemas import HealthCenterCreate , HealthCenterUpdate # Asegúrate de que esta línea esté presente # Asegúrate de que esta línea esté presente
from constants import countries

# Helper function to convert MongoDB documents to Pydantic-compatible format
def convert_objectid_to_str(data):
    """Converts ObjectId to string in a document."""
    if isinstance(data, list):
        return [convert_objectid_to_str(item) for item in data]
    elif isinstance(data, dict):
        return {key: str(value) if isinstance(value, ObjectId) else value for key, value in data.items()}
    return data


def get_heatmap_data(db: Collection) -> List[schemas.CovidData]:
    try:
        repo = CovidDataRepository(db)
        data = repo.get_heatmap_data()
        
        # Convertir los datos al formato esperado
        formatted_data = []
        for item in data:
            formatted_item = schemas.CovidData(
                country=item["country"],
                new_cases=int(item.get("new_cases", 0)),
                cumulative_cases=int(item.get("cumulative_cases", 0)),
                new_deaths=int(item.get("new_deaths", 0)),
                cumulative_deaths=int(item.get("cumulative_deaths", 0))
            )
            formatted_data.append(formatted_item)
        
        return formatted_data
    except Exception as e:
        print(f"Error getting heatmap data: {e}")
        return []

def create_health_center(db, center: HealthCenterCreate):
    try:
        # Convertir el modelo Pydantic a diccionario
        center_dict = center.model_dump(exclude_unset=True)
        
        # Asegurarse de que los campos requeridos estén presentes
        required_fields = ['name', 'address', 'phone_number', 'services', 'latitude', 'longitude']
        for field in required_fields:
            if field not in center_dict or center_dict[field] is None:
                raise ValueError(f"Missing required field: {field}")

        # Insertar en la base de datos
        collection = get_collection("health_centers")
        result = collection.insert_one(center_dict)
        
        # Obtener el documento insertado
        created_center = collection.find_one({"_id": result.inserted_id})
        if created_center:
            created_center["_id"] = str(created_center["_id"])
        return created_center
    except Exception as e:
        print(f"Error creating health center: {e}")
        return None


# def get_health_centers(skip: int = 0, limit: int = 100):
#     collection = get_collection("health_centers")
#     # Get total count first
#     total = collection.count_documents({})
    
#     # Get paginated results and convert ObjectId to string
#     centers = list(collection.find().skip(skip).limit(limit))
#     for center in centers:
#         if '_id' in center:
#             center['_id'] = str(center['_id'])
    
#     return {
#         "centers": centers,
#         "total": total
#     }

def get_health_centers(skip: int = 0, limit: int = 100, country: Optional[str] = None, services: Optional[str] = None):
    collection = get_collection("health_centers")
    query = {}
    
    if country and country != "":
        coords = countries.get(country)
        if coords:
            query["latitude"] = coords[0]
            query["longitude"] = coords[1]
    
    if services and services != "":
        query["services"] = services

    centers = list(collection.find(query).skip(skip).limit(limit))
    return centers

def update_health_center(db, center_id: str, center_update: dict):
    try:
        # Convertir el ID a ObjectId
        object_id = ObjectId(center_id)
        
        # Filtrar campos no nulos
        update_data = {k: v for k, v in center_update.items() if v is not None}
        
        # Realizar la actualización
        result = db["health_centers"].update_one(
            {"_id": object_id},
            {"$set": update_data}
        )
        
        if result.modified_count:
            # Obtener el documento actualizado
            updated_doc = db["health_centers"].find_one({"_id": object_id})
            if updated_doc:
                # Convertir ObjectId a string
                updated_doc["_id"] = str(updated_doc["_id"])
            return updated_doc
        return None
    except Exception as e:
        print(f"Error updating health center: {e}")
        return None

def remove_health_center(db, center_id: str):
    try:
        # Convertir el string ID a ObjectId
        object_id = ObjectId(center_id)
        collection = get_collection("health_centers")
        result = collection.delete_one({"_id": object_id})
        return result.deleted_count > 0
    except Exception as e:
        print(f"Error deleting health center: {e}")
        return False








# # Función para obtener datos de COVID por país
# def get_covid_data_by_country(db: Session, country: str):
#     repo = CovidDataRepository(db)
#     data = repo.get_by_country(country)
#     if data:
#         return {
#             'country': data.country,
#             'new_cases': data.new_cases or 0,
#             'cumulative_cases': data.cumulative_cases or 0,
#             'new_deaths': data.new_deaths or 0,
#             'cumulative_deaths': data.cumulative_deaths or 0,
#         }
#     return None


# # Función para obtener datos para el mapa de calor
# def get_heatmap_data(db: Session):
#     repo = CovidDataRepository(db)
#     data = repo.get_heatmap_data()
#     return [
#         {
#             'country': item.country,
#             'cumulative_cases': item.cumulative_cases or 0,
#             'cumulative_deaths': item.cumulative_deaths or 0,
#             'new_cases': item.new_cases or 0,
#             'new_deaths': item.new_deaths or 0,
#         }
#         for item in data
#     ]


# # Funciones CRUD para HealthCenter
# def create_health_center(db: Session, health_center: schemas.HealthCenterCreate):
#     repo = HealthCenterRepository(db)
#     db_center = HealthCenter(**health_center.dict())
#     return repo.add(db_center)


# def get_health_centers(db: Session, skip: int = 0, limit: int = 10, services: Optional[str] = None):
#     repo = HealthCenterRepository(db)
#     return repo.get_with_filter(services=services, skip=skip, limit=limit)


# def update_health_center(db: Session, center_id: int, updated_data: schemas.HealthCenterUpdate):
#     repo = HealthCenterRepository(db)
#     center = repo.get(HealthCenter, center_id)
#     if not center:
#         return None

#     for key, value in updated_data.dict(exclude_unset=True).items():
#         setattr(center, key, value)

#     return repo.update(center)


# def delete_health_center(db: Session, center_id: int):
#     repo = HealthCenterRepository(db)
#     center = repo.get(HealthCenter, center_id)
#     if not center:
#         return False

#     repo.delete(center)
#     return True