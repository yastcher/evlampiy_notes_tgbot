from src.config import ENGLISH, RUSSIAN, SPAIN, GERMAN

translates = {
    "success": {
        ENGLISH: "Success",
        RUSSIAN: "Успешно",
        SPAIN: "Éxito",
        GERMAN: "Erfolg",
    },
    "not_found": {
        ENGLISH: "Not found",
        RUSSIAN: "Не найден",
        SPAIN: "No encontrado",
        GERMAN: "Nicht gefunden",
    },
    "error_connection": {
        ENGLISH: "Connection error. Try later",
        RUSSIAN: "Ошибка соединения. Попробуйте позднее",
        SPAIN: "Error de conexión. Inténtalo más tarde",
        GERMAN: "Verbindungsfehler. Versuchen Sie es später",
    },
    "bad_data": {
        ENGLISH: "Bad data",
        RUSSIAN: "Неверные данные",
        SPAIN: "Datos incorrectos",
        GERMAN: "Schlechte Daten",
    },
    "choose_my_language": {
        ENGLISH: "Selected language: English",
        RUSSIAN: "Выбранный язык: Русский",
        SPAIN: "Idioma seleccionado: Español",
        GERMAN: "Ausgewählte Sprache: Deutsch",
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
