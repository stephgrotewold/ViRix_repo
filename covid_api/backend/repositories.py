# from sqlalchemy.orm import Session
from models import HealthCenter, CovidData
# from sqlalchemy import func
# from sqlalchemy.exc import SQLAlchemyError
from pymongo.collection import Collection
from bson import ObjectId
from schemas import HealthCenterCreate  # Asegúrate de que esta línea esté presente

class BaseRepository:
    def __init__(self, collection: Collection):
        self.collection = collection  # Cambiar db a collection

    def add(self, entity_data: dict):
        result = self.collection.insert_one(entity_data)
        return self.get(result.inserted_id)

    def get(self, entity_id: str):
        data = self.collection.find_one({"_id": ObjectId(entity_id)})
        return data if data else None

    def get_all(self, skip: int = 0, limit: int = 10):
        data = self.collection.find().skip(skip).limit(limit)
        return list(data)

    def update(self, entity_id: str, update_data: dict):
        result = self.collection.update_one({"_id": ObjectId(entity_id)}, {"$set": update_data})
        if result.matched_count:
            return self.get(entity_id)
        return None

    def delete(self, entity_id: str):
        result = self.collection.delete_one({"_id": ObjectId(entity_id)})
        return result.deleted_count > 0

class HealthCenterRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def add(self, entity_data: dict):
        result = self.collection.insert_one(entity_data)
        return self.get(result.inserted_id)

    def get(self, entity_id: str):
        data = self.collection.find_one({"_id": ObjectId(entity_id)})
        return data if data else None

    def get_all_paginated(self, skip: int = 0, limit: int = 1000):
        results = self.collection.find().skip(skip).limit(limit)
        return list(results)

    def update(self, entity_id: str, update_data: dict):
        result = self.collection.update_one({"_id": ObjectId(entity_id)}, {"$set": update_data})
        if result.matched_count:
            return self.get(entity_id)
        return None

    def delete(self, entity_id: str):
        result = self.collection.delete_one({"_id": ObjectId(entity_id)})
        return result.deleted_count > 0

class CovidDataRepository(BaseRepository):
    def get_heatmap_data(self):
        try:
            pipeline = [
                {
                    "$group": {
                        "_id": "$country",
                        "cumulative_cases": {"$max": "$cumulative_cases"},
                        "cumulative_deaths": {"$max": "$cumulative_deaths"},
                        "new_cases": {"$sum": "$new_cases"},
                        "new_deaths": {"$sum": "$new_deaths"}
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "country": "$_id",
                        "cumulative_cases": {"$ifNull": ["$cumulative_cases", 0]},
                        "cumulative_deaths": {"$ifNull": ["$cumulative_deaths", 0]},
                        "new_cases": {"$ifNull": ["$new_cases", 0]},
                        "new_deaths": {"$ifNull": ["$new_deaths", 0]}
                    }
                }
            ]
            return list(self.collection.aggregate(pipeline))
        except Exception as e:
            print(f"Error in get_heatmap_data: {e}")
            return []


# class BaseRepository:
#     def __init__(self, db: Session):
#         self.db = db

#     def add(self, entity):
#         try:
#             self.db.add(entity)
#             self.db.commit()
#             self.db.refresh(entity)
#             return entity
#         except SQLAlchemyError as e:
#             self.db.rollback()
#             raise e

#     def get(self, model, id: int):
#         return self.db.query(model).filter(model.id == id).first()

#     def get_all(self, model, skip: int = 0, limit: int = 10):
#         return self.db.query(model).offset(skip).limit(limit).all()

#     def update(self, entity):
#         try:
#             self.db.commit()
#             self.db.refresh(entity)
#             return entity
#         except SQLAlchemyError as e:
#             self.db.rollback()
#             raise e

#     def delete(self, entity):
#         try:
#             self.db.delete(entity)
#             self.db.commit()
#         except SQLAlchemyError as e:
#             self.db.rollback()
#             raise e


# class HealthCenterRepository(BaseRepository):
#     def __init__(self, db: Session):
#         super().__init__(db)

#     def get_by_name(self, name: str):
#         return self.db.query(HealthCenter).filter(HealthCenter.name == name).first()

#     def get_with_filter(self, services: str = None, skip: int = 0, limit: int = 10):
#         query = self.db.query(HealthCenter)
#         if services:
#             query = query.filter(HealthCenter.services == services)
#         return query.offset(skip).limit(limit).all()


# class CovidDataRepository(BaseRepository):
#     def __init__(self, db: Session):
#         super().__init__(db)

#     def get_by_country(self, country: str):
#         return self.db.query(CovidData).filter(CovidData.country == country).first()

#     def get_heatmap_data(self):
#         return self.db.query(
#             CovidData.country,
#             func.sum(CovidData.cumulative_cases).label('cumulative_cases'),
#             func.sum(CovidData.cumulative_deaths).label('cumulative_deaths'),
#             func.sum(CovidData.new_cases).label('new_cases'),
#             func.sum(CovidData.new_deaths).label('new_deaths')
#         ).group_by(CovidData.country).all()