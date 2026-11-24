# JK Bot Comercial — Sistemas JK

Dos componentes independientes:

1. **Demo web (`index.html`, `styles.css`, `app.js`)**: simulador interactivo de una conversación tipo Telegram que funciona en GitHub Pages, sin cuentas, claves ni servidor. Permite consultar precios y servicios ficticios, horarios, contacto y completar una solicitud simulada de cita. Los mensajes no salen del navegador, ni se guardan en una base de datos. No es un bot conectado a Telegram.
2. **Ejemplo de bot real (`bot.py`)**: bot de Python con la biblioteca estándar que se conecta a la Bot API de Telegram mediante long polling. Ofrece menú de servicios ficticios, precios, horarios y contacto. **No tiene flujo de reserva real** ni base de datos; sirve como ejemplo educativo y para pruebas autorizadas.

## Publicación del simulador

Sube `index.html`, `styles.css`, `app.js` y este `README.md` al directorio raíz de un repositorio público. En GitHub, ve a Settings → Pages, elige Deploy from a branch → main → / (root). No subas tokens, logs ni datos privados.

## Crear y ejecutar el bot real

1. Abre el BotFather oficial: https://t.me/BotFather y envía `/newbot`.
2. Configura su nombre y un username terminado en `bot`. BotFather te proporciona un **token secreto**.
3. Descarga `bot.py` en tu PC. Necesitas Python 3.9 o superior, con acceso a Internet. No necesitas instalar paquetes adicionales.
4. En Windows PowerShell, ejecuta (sustituyendo el marcador por el token privado, **solo localmente**):

```powershell
$env:TELEGRAM_BOT_TOKEN = 'TU_TOKEN_PRIVADO'
python bot.py
```

5. En Telegram, abre tu bot e inicia una conversación con `/start`. Permanecerá activo mientras Python siga abierto. Para detener, pulsa `Ctrl+C`.

**Seguridad:** nunca publiques el token en GitHub, páginas web o mensajes a terceros. Si lo filtras, revócalo inmediatamente desde BotFather. El bot de ejemplo no requiere administrar grupos, leer bases de datos ni recolectar información personal.

**Importante:** un bot siempre disponible necesita un proceso en ejecución (servidor, plataforma cloud o PC encendido). GitHub Pages por sí solo no puede alojar el programa Python.

**Uso:** demostración educativa y portafolio, no un sistema listo para producción.
