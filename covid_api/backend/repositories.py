from sqlalchemy.orm import Session
from models import HealthCenter, CovidData
from sqlalchemy import func

class BaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, entity):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def get(self, model, id: int):
        return self.db.query(model).filter(model.id == id).first()

    def get_all(self, model, skip: int = 0, limit: int = 10):
        return self.db.query(model).offset(skip).limit(limit).all()

    def update(self, entity):
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, entity):
        self.db.delete(entity)
        self.db.commit()

class HealthCenterRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_name(self, name: str):
        return self.db.query(HealthCenter).filter(HealthCenter.name == name).first()

class CovidDataRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_country(self, country: str):
        return self.db.query(CovidData).filter(CovidData.country == country).first()

    def get_heatmap_data(self):
        return self.db.query(
            CovidData.country,
            func.sum(CovidData.cumulative_cases).label('cumulative_cases'),
            func.sum(CovidData.cumulative_deaths).label('cumulative_deaths'),
            func.sum(CovidData.new_cases).label('new_cases'),
            func.sum(CovidData.new_deaths).label('new_deaths')
        ).group_by(CovidData.country).all()