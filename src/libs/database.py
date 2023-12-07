from pymongo import MongoClient
from bson import ObjectId
from src.libs.config import Settings as settings


class Database():

    def __init__(self) -> None:
        self.client = MongoClient(host="api-db", port=27017)
        self.db = self.client["todolist-db"]

    def find_tasks(self):
        try:
            result = list(self.db[
                    settings.COLLECTION_TASKS].find())
            for item in result:
                item["_id"] = str(item["_id"])
            return result
        except Exception as err:
            print("Error: ", err)
            return None

    def find_task(self, id):
        try:
            result = self.db[
                settings.COLLECTION_TASKS].find_one({"_id": ObjectId(id)})
            if result:
                result["_id"] = str(result["_id"])
                return result
            return None
        except Exception as err:
            print("Error: ", err)
            return None

    def create_task(self, payload):
        try:
            result = self.db[settings.COLLECTION_TASKS].insert_one(
                    payload.dict()).inserted_id
            task = self.find_task(result)
            return task
        except Exception as err:
            print("Error: ", err)
            return None

    def update_task(self, id, payload):
        try:
            result = self.db[
                settings.COLLECTION_TASKS].update_one(
                {"_id": ObjectId(id)},
                {"$set": payload.dict()}).modified_count
            if result > 0:
                task = self.find_task(id)
                return task
            return None
        except Exception as err:
            print("Error: ", err)
            return None

    def delete_task(self, id):
        try:
            result = self.db[
                settings.COLLECTION_TASKS].delete_one(
                {"_id": ObjectId(id)}).deleted_count
            if result > 0:
                return {"ok": True}
            return False
        except Exception as err:
            print("Error: ", err)
            return False
