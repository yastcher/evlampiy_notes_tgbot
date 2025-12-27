import time

import requests

from src.mongo import set_github_settings

GITHUB_DEVICE_CODE_URL = "https://github.com/login/device/code"
GITHUB_OAUTH_TOKEN_URL = "https://github.com/login/oauth/access_token"


def get_github_device_code(client_id: str, scopes: str = "repo") -> dict:
    data = {"client_id": client_id, "scope": scopes}
    headers = {"Accept": "application/json"}
    resp = requests.post(GITHUB_DEVICE_CODE_URL, data=data, headers=headers)
    return resp.json()  # device_code, user_code, verification_uri, expires_in, interval


def poll_github_for_token(client_id: str, device_code: str) -> str | None:
    headers = {"Accept": "application/json"}
    while True:
        data = {
            "client_id": client_id,
            "device_code": device_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        }
        resp = requests.post(GITHUB_OAUTH_TOKEN_URL, data=data, headers=headers)
        j = resp.json()

        if "error" not in j:
            return j["access_token"]

        error = j["error"]
        if error == "authorization_pending":
            time.sleep(5)
            continue
        elif error == "slow_down":
            time.sleep(10)
            continue
        elif error in ("expired_token", "access_denied"):
            return
        else:
            return


async def authorize_github_for_user(update, context):
    client_id = "Ваша_учетная_запись_GitHub_OAuthApp"
    device_info = get_github_device_code(client_id)
    verification_uri = device_info["verification_uri"]
    user_code = device_info["user_code"]
    expires_in = device_info["expires_in"]
    interval = device_info["interval"]

    # todo =Y delete it - it is only for ruff
    chat_id = interval

    message = (
        f"1) Откройте страницу: {verification_uri}\n"
        f"2) Введите код: {user_code}\n"
        f"У вас есть ~{expires_in} секунд.\n"
        "После подтверждения я получу доступ к вашему GitHub (scope=repo)."
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

    token = poll_github_for_token(client_id, device_info["device_code"])
    if token:
        await set_github_settings(chat_id, "", "", token)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Успешно! Ваш токен: " + token[:10] + "...",
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Авторизация не состоялась (timeout / denied).",
        )
