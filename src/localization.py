ENGLISH = "en"
RUSSIAN = "ru"
LANGUAGES = (ENGLISH, RUSSIAN, )

translates = {
    "success": {
        ENGLISH: "Success",
        RUSSIAN: "Успешно",
    },
    "not_found": {
        ENGLISH: "Not found",
        RUSSIAN: "Не найден",
    },
    "error_connection": {
        ENGLISH: "Connection error. Try later",
        RUSSIAN: "Ошибка соединения. Попробуйте позднее",
    },
    "bad_data": {
        ENGLISH: "Bad data",
        RUSSIAN: "Неверные данные",
    },
}


def get_translate(message_key: str, lang: str, args: tuple = ()) -> str:
    """
    possible to send message_key or message
    if message_key not present in translates then return pure source message
    else return formatted and translated message
    """
    message: str = translates.get(message_key, {}).get(lang, message_key)
    return message % args
