from models import HealthCenter, CovidData
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
