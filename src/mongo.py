from pymongo import MongoClient

from src.config import settings

client = MongoClient(settings.mongo_uri)
db = client.user_settings_db
collection = db.user_settings


def set_user_language(user_id, language):
    collection.update_one(
        {"user_id": user_id},
        {"$set": {"language": language}},
        upsert=True
    )


def get_user_language(user_id):
    user = collection.find_one({"user_id": user_id})
    return user.get("language", settings.default_language) if user else settings.default_language


def set_user_chatgpt_key(user_id, key):
    collection.update_one(
        {"user_id": user_id},
        {"$set": {"chatgpt_key": key}},
        upsert=True
    )


def get_user_chatgpt_key(user_id):
    user = collection.find_one({"user_id": user_id})
    return user.get("chatgpt_key") if user else None
