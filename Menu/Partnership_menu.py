import CONSTANT
from Menu.Menu import Menu
import telebot

class Partnership_menu(Menu): # Сотруднечиство
    def __init__(self, message, userdata,  bot, regular_id = None):
        super().__init__(message = message, userdata = userdata, bot = bot, state = CONSTANT.NAME_PARTNERSHIP_MENU, regular_id = regular_id)
    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Зказкать услугу')
        keyboard.row('Виполнить услугу')
        keyboard.row('Назад')
        self.bot.send_message(self.regular_id, 'Введіть прізвище', reply_markup = keyboard)
    def press(self, message):
        if message.text == 'Назад':
            from Menu.Start_menu import Start_menu
            menu = Start_menu(message, self.userdata, self.bot)
            return menu
        return self