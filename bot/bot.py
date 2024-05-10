import asyncio

# filters
from tgbot.filters.admin_filter import AdminFilter

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import any_user, get_product

# middlewares
from tgbot.middlewares.antiflood_middleware import AntiFloodMiddleware

# states
from tgbot.states.register_state import Register

# utils
from tgbot.utils.database import Database

# telebot
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_filters import TextMatchFilter

# config
from tgbot import config

from tgbot.markups.markup import BuildMarkup

markup = BuildMarkup()


bot = AsyncTeleBot(config.TOKEN)


def register_handlers():
    bot.register_message_handler(admin_user, commands=['start'],
                                 admin=True, pass_bot=True)
    bot.register_message_handler(any_user, commands=['start'],
                                 admin=False, pass_bot=True)
    bot.register_message_handler(anti_spam, commands=['spam'], pass_bot=True)

    bot.register_message_handler(get_product, text=[markup.get_text('get_product')], pass_bot=True)


register_handlers()

# Middlewares
bot.setup_middleware(AntiFloodMiddleware(limit=2, bot=bot))


# custom filters
bot.add_custom_filter(AdminFilter())
bot.add_custom_filter(TextMatchFilter())



async def run():
    await bot.polling(non_stop=True)


asyncio.run(run())

asyncio.run(run())
