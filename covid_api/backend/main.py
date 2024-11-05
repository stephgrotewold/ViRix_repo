from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pymongo.database import Database
from bson import ObjectId
from config import get_database, get_collection
import crud
from constants import countries
from schemas import (
    HealthCenterCreate,
    HealthCenterUpdate,
)

app = FastAPI()
db = get_database()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la base de datos
def get_db():
    return db

def convert_objectid(item):
    if isinstance(item, dict):
        for key, value in item.items():
            if isinstance(value, ObjectId):
                item[key] = str(value)
            elif isinstance(value, dict):
                convert_objectid(value)
            elif isinstance(value, list):
                for i in value:
                    if isinstance(i, dict):
                        convert_objectid(i)
    return item

@app.get("/health_centers/")
def get_health_centers(
    skip: int = 0,
    limit: int = 100,
    country: Optional[str] = None,
    services: Optional[str] = None,
    db: Database = Depends(get_database)
):
    query = {}
    
    if country and country != "":
        # Buscar por coordenadas del país
        coords = countries.get(country)
        if coords:
            query["latitude"] = coords[0]
            query["longitude"] = coords[1]
    
    if services and services != "":
        query["services"] = services

    try:
        centers = list(db["health_centers"].find(query).skip(skip).limit(limit))
        # Convertir ObjectId a string
        centers = [convert_objectid(center) for center in centers]
        total = db["health_centers"].count_documents(query)
        return {"centers": centers, "total": total}
    except Exception as e:
        print(f"Error: {str(e)}")  # Para depuración
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/health_centers/")
async def create_health_center(
    health_center: HealthCenterCreate,
    db: Database = Depends(get_database)
):
    try:
        created_center = crud.create_health_center(db, health_center)
        if not created_center:
            raise HTTPException(
                status_code=500,
                detail="Error creating health center"
            )
        return created_center
    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )

@app.put("/health_centers/{center_id}")
async def update_health_center(
    center_id: str,
    center: HealthCenterUpdate,
    db: Database = Depends(get_database)
):
    try:
        # Convertir el modelo Pydantic a diccionario
        update_data = center.model_dump(exclude_unset=True)
        
        # Actualizar el centro de salud
        updated_center = crud.update_health_center(db, center_id, update_data)
        
        if not updated_center:
            raise HTTPException(
                status_code=404,
                detail="Health center not found or no changes applied"
            )
        return updated_center
    except Exception as e:
        raise HTTPException(
            status_code=422,
            detail=f"Could not update health center: {str(e)}"
        )

@app.delete("/health_centers/{center_id}")
async def delete_health_center(
    center_id: str,
    db: Database = Depends(get_database)
):
    try:
        if not ObjectId.is_valid(center_id):
            raise HTTPException(
                status_code=422,
                detail="Invalid center ID format"
            )
        
        success = crud.remove_health_center(db, center_id)
        if success:
            return {"message": "Health center deleted successfully"}
        else:
            raise HTTPException(
                status_code=404,
                detail="Health center not found"
            )
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/heatmap-data")
def get_heatmap_data(db: Database = Depends(get_db)):
    try:
        collection = db["covid_data"]
        data = crud.get_heatmap_data(collection)
        
        if not data:
            print("No heatmap data found")
            return []
            
        print(f"Returning {len(data)} records for heatmap")
        return data
    except Exception as e:
        print(f"Error in heatmap endpoint: {e}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
