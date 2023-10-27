import telegram
from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes

from src.application.telegram_bot.constants.messages import back, welcome, unknown_command


def register_text_handlers(app):
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    response = unknown_command
    if text == back:
        response = welcome

    await update.message.reply_text(response, parse_mode=telegram.constants.ParseMode.MARKDOWN)
