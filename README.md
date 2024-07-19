# FilesFacuBot

FilesFacuBot es un bot de Telegram diseñado para facilitar el envío y almacenamiento de archivos relacionados con la facultad. Permite a los usuarios solicitar archivos específicos y subir nuevos archivos para su almacenamiento y posterior recuperación.

## Comandos

-  `/start`**: Inicia la conversación.
-  `/send [nombre de archivo.extension]`**: Envía un archivo solicitado por el usuario, siempre y cuando esté disponible en la carpeta especificada.

## Requisitos

- Python 3.7 o superior
- Bibliotecas de Python:
  - `python-telegram-bot`

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tuusuario/filesfacubot.git
    cd filesfacubot
    ```

2. Crea un entorno virtual y activa el entorno:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Coloca tus archivos en la carpeta `files` en la raíz del proyecto.

5. Configura tu token de bot y nombre de usuario en el código:

    ```python
    TOKEN: Final = "TU_TOKEN_DE_TELEGRAM"
    BOT_USERNAME: Final = "@TuNombreDeUsuarioBot"
    ```

## Uso

Para iniciar el bot, ejecuta el siguiente comando:

```bash
python bot.py
