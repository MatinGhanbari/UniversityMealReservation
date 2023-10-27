import telegram
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from src.application.telegram_bot.constants.messages import start_command, help_command, welcome, help


def register_command_handlers(app):
    app.add_handler(CommandHandler(start_command, reply_start_command))
    app.add_handler(CommandHandler(help_command, reply_help_command))


async def reply_start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(welcome, parse_mode=telegram.constants.ParseMode.MARKDOWN)


async def reply_help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(help)
