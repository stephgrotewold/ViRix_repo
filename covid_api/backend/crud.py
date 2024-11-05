from typing import Optional, List
from pymongo.collection import Collection
from bson import ObjectId
from repositories import CovidDataRepository
import schemas
from config import get_collection, get_database
from database import db
from schemas import HealthCenterCreate
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
