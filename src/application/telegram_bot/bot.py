from telegram import Update
from telegram.ext import Application, ContextTypes

from src.bootstrapper.service_registrar import ServiceRegistrar
from src.infrastructure.config import Config
from src.main import container


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


def start_bot():
    ServiceRegistrar.register_services()
    config = container.resolve(Config)
    print('Starting telegram_bot...')

    app = Application.builder().token(config.api_key).build()

    from src.application.telegram_bot.command_handlers import register_command_handlers
    register_command_handlers(app)
    from src.application.telegram_bot.text_handlers import register_text_handlers
    register_text_handlers(app)

    app.add_error_handler(error)

    app.run_polling(poll_interval=3)
