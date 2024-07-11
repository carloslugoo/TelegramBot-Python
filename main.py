from typing import Final
from telegram import Update

import os

from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
TOKEN: Final = "6329249838:AAHXqAIu8fuhSiiW08gN83Gn-EaW-lEH95o"
BOT_USERNAME: Final = "@FilesFacuBot"

SECRET_PASSWORD = "testt"
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Te paso tus archivos de la Facu con /send [nombre de archivo.extension] o te guardo los archivos")


async def send_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Verificar si el usuario proporcionó un nombre de archivo
    if len(context.args) == 0:
        await update.message.reply_text("Debes proporcionar el nombre del archivo que deseas enviar.")
        return

    # Obtener el nombre del archivo especificado por el usuario
    file_name = context.args[0]

    # Especifica la carpeta donde se encuentran los archivos que deseas enviar
    folder_path = "./files/" 

    # Verifica si el archivo existe en la carpeta
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(file_path):
        await update.message.reply_text(f"El archivo '{file_name}' no se encontró en la carpeta especificada.")
        return

    # Envía el archivo al usuario
    await update.message.reply_document(open(file_path, 'rb'), caption=f"Aquí tienes tu archivo: {file_name}")


if __name__ == "__main__":
    print("Bot iniciado..")
    # Crear una instancia de la aplicación
    app = Application.builder().token(TOKEN).build()

    # Registra los manejadores de comandos
    start_handler = CommandHandler("start", start_command)
    send_handler = CommandHandler("send", send_command)
  
    app.add_handler(start_handler)
    app.add_handler(send_handler)

    app.run_polling()
