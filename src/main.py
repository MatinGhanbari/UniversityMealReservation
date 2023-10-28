from src.infrastructure.container import Container

container = Container()

if __name__ == '__main__':
    from src.application.telegram_bot import bot

    bot.start_bot()
