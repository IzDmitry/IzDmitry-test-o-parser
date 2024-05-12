from telebot import types


TEXT_BUTTONS_RUS = {
    'get_product': 'Список товаров',
    'follow': 'Отслеживать парсинг'
}


class BuildMarkup:

    def __init__(self, code='ru'):
        if code == 'ru':
            self.text_btn = TEXT_BUTTONS_RUS

    def get_text(self, key):
        return self.text_btn.get(key)

    def get_button(self, key):
        return types.KeyboardButton(self.text_btn[key])

    def get_inline_button(self, key, callback_data=None, pay=None):
        return types.InlineKeyboardButton(self.text_btn[key],
                                          callback_data=callback_data)

    def main_menu(self):
        markup = types.ReplyKeyboardMarkup(row_width=1,
                                           resize_keyboard=True)
        return markup.add(
            self.get_button('get_product'),
            self.get_button('follow'),
        )
