from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, CallbackQuery
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from tgbot.states.register_state import Register
from tgbot.utils.database import Database
from tgbot.markups.markup import BuildMarkup

markup = BuildMarkup()
db = Database()


async def any_user(message: Message, bot: AsyncTeleBot):
    """
    You can create a function and use parameter pass_bot.

    """

    try:
        text = 'Выберите действие'
        print(db.get_products())
        await bot.send_message(message.chat.id, text,
                               reply_markup=markup.main_menu())
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


async def get_product(message: Message, bot: AsyncTeleBot):
    try:
        products = db.get_products()

        text = f"Результат последнего парсинга:\n\nДата:\n\n"  # Вставляем пустую переменную date
        
        count = 1
        for product in products.values():
            product['name'] = product['name'].replace("-", "\-")
            product['url'] = product['url'].replace("-", "\-")
            text += f"{count}\. {product['name']} [ссылка]({product['url']})\n\n"
            count += 1
            date = product['date']
        
        text = text.replace("Дата:\n\n", f"Дата: {date.strftime('%d/%m/%Y')}\n\n")  
        
        await bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
    
    except (ConnectionError, TimeoutError, TooManyRedirects) as e:
        print(e)











