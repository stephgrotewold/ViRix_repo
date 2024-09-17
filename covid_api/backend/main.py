from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
import models, schemas, crud
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las URLs, puedes restringir a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/covid-data", response_model=schemas.CovidData)
def read_covid_data(location: str, db: Session = Depends(get_db)):
    data = crud.get_covid_data_by_country(db, country=location)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@app.get("/heatmap-data", response_model=List[schemas.CovidData])
def get_heatmap_data(db: Session = Depends(get_db)):
    try:
        # Obtener datos agregados por país sin el campo 'risk_level'
        data = db.query(
            models.CovidData.country,
            func.sum(models.CovidData.cumulative_cases).label('cumulative_cases'),
            func.sum(models.CovidData.cumulative_deaths).label('cumulative_deaths'),
            func.sum(models.CovidData.new_cases).label('new_cases'),
            func.sum(models.CovidData.new_deaths).label('new_deaths')
        ).group_by(models.CovidData.country).all()
        
        if not data:
            raise HTTPException(status_code=404, detail="Data not found")
        
        return data

    except Exception as e:
        # Captura y muestra el error en la consola
        print(f"Error al obtener los datos: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")