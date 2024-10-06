from sqlalchemy.orm import Session
from sqlalchemy import func
import models, schemas
from repositories import HealthCenterRepository, CovidDataRepository
from line_profiler import profile

@profile
# Función para obtener datos de COVID por país
def get_covid_data_by_country(db: Session, country: str):
    # Agrupa y suma los valores por país
    data = db.query(
        models.CovidData.country,
        func.sum(models.CovidData.new_cases).label('new_cases'),
        func.sum(models.CovidData.cumulative_cases).label('cumulative_cases'),
        func.sum(models.CovidData.new_deaths).label('new_deaths'),
        func.sum(models.CovidData.cumulative_deaths).label('cumulative_deaths')
    ).filter(models.CovidData.country == country).group_by(models.CovidData.country).first()

    if data:
        # Reemplaza los valores nulos (None) por 0
        return {
            'country': data.country,
            'new_cases': data.new_cases if data.new_cases is not None else 0,
            'cumulative_cases': data.cumulative_cases if data.cumulative_cases is not None else 0,
            'new_deaths': data.new_deaths if data.new_deaths is not None else 0,
            'cumulative_deaths': data.cumulative_deaths if data.cumulative_deaths is not None else 0,
        }
    return None

# Función para obtener datos para el mapa de calor
@profile
def get_heatmap_data(db: Session):
    data = db.query(
        models.CovidData.country,
        func.sum(models.CovidData.cumulative_cases).label('cumulative_cases'),
        func.sum(models.CovidData.cumulative_deaths).label('cumulative_deaths'),
        func.sum(models.CovidData.new_cases).label('new_cases'),
        func.sum(models.CovidData.new_deaths).label('new_deaths')
    ).group_by(models.CovidData.country).all()

    if data:
        return [
            {
                'country': item.country,
                'cumulative_cases': item.cumulative_cases if item.cumulative_cases is not None else 0,
                'cumulative_deaths': item.cumulative_deaths if item.cumulative_deaths is not None else 0,
                'new_cases': item.new_cases if item.new_cases is not None else 0,
                'new_deaths': item.new_deaths if item.new_deaths is not None else 0,
            }
            for item in data
        ]
    return []

# Funciones CRUD para HealthCenter
@profile
def create_health_center(db: Session, health_center: schemas.HealthCenterCreate):
    repo = HealthCenterRepository(db)
    db_center = models.HealthCenter(**health_center.dict())
    return repo.add(db_center)

@profile
def get_health_centers(db: Session, skip: int = 0, limit: int = 10):
    repo = HealthCenterRepository(db)
    return repo.get_all(models.HealthCenter, skip, limit)

@profile
def update_health_center(db: Session, center_id: int, updated_data: schemas.HealthCenterUpdate):
    repo = HealthCenterRepository(db)
    center = repo.get(models.HealthCenter, center_id)
    
    # Comprobación para asegurarse de que el centro existe
    if not center:
        return None
    
    # Actualización de los campos disponibles
    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(center, key, value)
    
    return repo.update(center)

@profile
def delete_health_center(db: Session, center_id: int):
    repo = HealthCenterRepository(db)
    center = repo.get(models.HealthCenter, center_id)
    
    # Comprobación para asegurarse de que el centro existe
    if not center:
        return False
    
    repo.delete(center)
    return True