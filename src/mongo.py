from pymongo import MongoClient

from src.config import settings

client = MongoClient(settings.mongo_uri)
db = client["user_settings"]
users_collection = db["users"]


def set_user_language(user_id, language):
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"language": language}},
        upsert=True,
    )


def get_user_language(user_id):
    user = users_collection.find_one({"user_id": user_id})
    return user.get("language", settings.default_language) if user else settings.default_language
