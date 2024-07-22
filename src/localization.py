from src.config import ENGLISH, RUSSIAN, SPAIN

translates = {
    "success": {
        ENGLISH: "Success",
        RUSSIAN: "Успешно",
        SPAIN: "Éxito",
    },
    "not_found": {
        ENGLISH: "Not found",
        RUSSIAN: "Не найден",
        SPAIN: "No encontrado",
    },
    "error_connection": {
        ENGLISH: "Connection error. Try later",
        RUSSIAN: "Ошибка соединения. Попробуйте позднее",
        SPAIN: "Error de conexión. Inténtalo más tarde",
    },
    "bad_data": {
        ENGLISH: "Bad data",
        RUSSIAN: "Неверные данные",
        SPAIN: "Datos incorrectos",
    },
    "choose_language": {
        ENGLISH: "Selected language: English",
        RUSSIAN: "Выбранный язык: Русский",
        SPAIN: "Idioma seleccionado: Español",
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
