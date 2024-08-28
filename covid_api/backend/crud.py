from sqlalchemy.orm import Session
import models

def get_covid_data_by_country(db: Session, country: str):
    data = db.query(models.CovidData).filter(models.CovidData.country == country).first()
    if data:
        # Reemplaza los valores nulos (None) por 0 o una cadena vacía
        data.new_cases = data.new_cases if data.new_cases is not None else 0
        data.cumulative_cases = data.cumulative_cases if data.cumulative_cases is not None else 0
        data.new_deaths = data.new_deaths if data.new_deaths is not None else 0
        data.cumulative_deaths = data.cumulative_deaths if data.cumulative_deaths is not None else 0
    return data