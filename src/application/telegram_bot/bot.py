import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from src.application.telegram_bot.command_handlers import register_command_handlers
from src.bootstrapper.service_registrar import ServiceRegistrar
from src.infrastructure.config import Config
from src.infrastructure.container import Container

container = Container()
ServiceRegistrar(container=container).register_services()
config = container.resolve(Config)




async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    user_message: str = update.message.text

    print(f'User {update.message.chat.id} in {message_type}: "{user_message}')

    response = "Hello 🙋‍♀️!"

    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


def start_bot():
    print('Starting telegram_bot...')

    app = Application.builder().token(config.api_key).build()

    register_command_handlers(app)

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=3)
