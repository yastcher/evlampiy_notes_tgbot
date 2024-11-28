import asyncio

from pymongo import MongoClient

from src.config import settings

mongo_client = MongoClient(settings.mongo_uri)
db = mongo_client["user_settings"]
users_collection = db["users"]


async def set_chat_language(chat_id: str, language: str):
    await asyncio.to_thread(
        users_collection.update_one,
        {"chat_id": chat_id},
        {"$set": {"language": language}},
        upsert=True,
    )


async def get_chat_language(chat_id: str) -> str:
    chat_settings = await asyncio.to_thread(
        users_collection.find_one,
        {"chat_id": chat_id},
    )
    return chat_settings.get("language", settings.default_language) if chat_settings else settings.default_language


async def set_gpt_command(chat_id: str, command: str):
    await asyncio.to_thread(
        users_collection.update_one,
        {"chat_id": chat_id},
        {"$set": {"command": command}},
        upsert=True,
    )


async def get_gpt_command(chat_id: str) -> str:
    chat_settings = await asyncio.to_thread(
        users_collection.find_one,
        {"chat_id": chat_id},
    )
    if chat_settings:
        return chat_settings.get("command", settings.telegram_bot_command)
    else:
        return settings.telegram_bot_command
