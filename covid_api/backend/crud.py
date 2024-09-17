from sqlalchemy.orm import Session
from sqlalchemy import func
import models

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

def get_covid_data_by_who_region(db: Session, who_region: str):
    return db.query(models.CovidData).filter(models.CovidData.who_region == who_region).all()