import CONSTANT
from Menu.Menu import Menu
import telebot

class Help_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id = None):
        super().__init__(message = message, userdata = userdata, bot = bot, state = CONSTANT.NAME_HELP_MENU, regular_id = regular_id)

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Кнопка')
        self.bot.send_message(self.regular_id, '---', reply_markup = keyboard)
    def press(self, message):
        if message.text == 'Назад':
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            return menu
        return self