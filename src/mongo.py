import asyncio

from pymongo import MongoClient

from src.config import settings

mongo_client = MongoClient(settings.mongo_uri)
db = mongo_client["user_settings"]
users_collection = db["users"]


async def set_user_language(user_id, language):
    await asyncio.to_thread(
        users_collection.update_one,
        {"user_id": user_id},
        {"$set": {"language": language}},
        upsert=True,
    )


async def get_user_language(user_id):
    user = await asyncio.to_thread(
        users_collection.find_one,
        {"user_id": user_id},
    )
    return user.get("language", settings.default_language) if user else settings.default_language


async def set_user_command(user_id, command):
    await asyncio.to_thread(
        users_collection.update_one,
        {"user_id": user_id},
        {"$set": {"command": command}},
        upsert=True,
    )


async def get_user_command(user_id):
    user = await asyncio.to_thread(
        users_collection.find_one,
        {"user_id": user_id},
    )
    return user.get("command", settings.telegram_bot_command) if user else settings.telegram_bot_command
