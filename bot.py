"""Bot real básico de Telegram con la biblioteca estándar de Python.

Uso:
  PowerShell: $env:TELEGRAM_BOT_TOKEN="TOKEN_SECRETO"
              python bot.py
  Bash:       TELEGRAM_BOT_TOKEN="TOKEN_SECRETO" python3 bot.py

El bot funciona mientras este programa esté ejecutándose.
No pegues tu token en el código ni lo subas a GitHub.
"""
import json
import logging
import os
import time
import urllib.error
import urllib.parse
import urllib.request

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
if not TOKEN:
    raise SystemExit("Falta TELEGRAM_BOT_TOKEN en las variables de entorno.")
BASE = f"https://api.telegram.org/bot{TOKEN}/"
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

SERVICIOS = "✂️ Servicios de ejemplo:\n• Corte clásico: S/ 25\n• Corte y barba: S/ 40\n• Tratamiento capilar: S/ 65"
MENU = {"inline_keyboard": [
    [{"text": "✂️ Servicios y precios", "callback_data": "servicios"}],
    [{"text": "📆 Reservas", "callback_data": "reservar"}, {"text": "🕒 Horarios", "callback_data": "horario"}],
    [{"text": "☎️ Contacto", "callback_data": "contacto"}],
]}

def api(method, payload=None, timeout=35):
    data = urllib.parse.urlencode(payload or {}).encode("utf-8")
    with urllib.request.urlopen(urllib.request.Request(BASE + method, data=data), timeout=timeout) as response:
        result = json.load(response)
    if not result.get("ok"):
        raise RuntimeError("La API de Telegram no confirmó la operación")
    return result["result"]

def send(chat_id, message, buttons=True):
    payload = {"chat_id": chat_id, "text": message}
    if buttons:
        payload["reply_markup"] = json.dumps(MENU, ensure_ascii=False)
    api("sendMessage", payload)

def response(cmd):
    if cmd in ("servicios", "precios", "/servicios", "/precios"):
        return SERVICIOS + "\n\nPrecios ficticios de demostración."
    if cmd in ("horario", "/horario"):
        return "🕒 Horario de ejemplo: lunes a sábado, de 9:00 a 19:00."
    if cmd in ("reservar", "/reservar"):
        return "📆 Esta versión muestra el flujo de reservas como ejemplo. No registra citas reales."
    if cmd in ("contacto", "/contacto"):
        return "☎️ Sistemas JK · https://webseodigital.es/"
    return "👋 ¡Hola! Soy JK Bot Comercial, un bot demostrativo. Selecciona una opción:"

def main():
    logging.info("Bot iniciado. Detén con Ctrl+C.")
    offset = None
    while True:
        try:
            args = {"timeout": 25, "allowed_updates": json.dumps(["message", "callback_query"])}
            if offset is not None:
                args["offset"] = offset
            updates = api("getUpdates", args, timeout=35)
            for update in updates:
                offset = update["update_id"] + 1
                callback = update.get("callback_query")
                if callback:
                    api("answerCallbackQuery", {"callback_query_id": callback["id"]})
                    message = callback.get("message", {})
                    chat_id = message.get("chat", {}).get("id")
                    command = callback.get("data", "")
                else:
                    message = update.get("message", {})
                    chat_id = message.get("chat", {}).get("id")
                    command = (message.get("text") or "").lower().split("@", 1)[0].strip()
                if chat_id:
                    send(chat_id, response(command))
        except KeyboardInterrupt:
            logging.info("Bot detenido")
            break
        except (urllib.error.URLError, TimeoutError, RuntimeError, OSError) as exc:
            logging.warning("Fallo de conexión o API: %s", type(exc).__name__)
            time.sleep(5)

if __name__ == "__main__":
    main()
