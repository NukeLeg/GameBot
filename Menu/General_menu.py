import CONSTANT
from Menu.Menu import Menu
import telebot


class General_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_GENERAL_MENU, regular_id=regular_id)

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Профіль', 'Пошта')
        keyboard.row('Казино', 'На вулицю')
        self.bot.send_message(self.regular_id, 'Головне меню', reply_markup=keyboard)

    def press(self, message):
        if message.text == 'Профіль':
            from Menu.Home.Home_menu import Home_menu
            menu = Home_menu(message, self.userdata, self.bot)
            return menu
        if message.text == 'Казино':
            from Menu.Casino.Casino_menu import Casino_menu
            menu = Casino_menu(message, self.userdata, self.bot)
            return menu
        return self