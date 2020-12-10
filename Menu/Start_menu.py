import CONSTANT
from Menu.Menu import Menu
import telebot

class Start_menu(Menu): # Старт меню
    def __init__(self, message, userdata, bot, regular_id = None):
        super().__init__(message = message, userdata = userdata, bot = bot, state = CONSTANT.NAME_START_MENU, regular_id = regular_id)
    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Поиск', 'Добавити')
        keyboard.row('Сотруднечиство')
        keyboard.row('Помощь', 'О проекте')
        self.bot.send_message(self.regular_id, 'Начали!!!', reply_markup = keyboard)
    def press(self, message):
        if message.text == 'Поиск':
            from Menu.Search_menu import Search_menu
            menu = Search_menu(message, self.userdata, self.bot)
            return menu
        elif message.text == 'Сотруднечиство':
            from Menu.Partnership_menu import Partnership_menu
            menu = Partnership_menu(message, self.userdata, self.bot)
            return menu
        elif message.text == 'Добавити':
            from Menu.Add_menu import Add_menu
            menu = Add_menu(message, self.userdata, self.bot)
            return menu
        elif message.text == 'Помощь':
            from Menu.Help_menu import Help_menu
            menu = Help_menu(message, self.userdata, self.bot)
            return menu
        elif message.text == 'О проекте':
            from Menu.About_menu import About_menu
            menu = About_menu(message, self.userdata, self.bot)
            return menu
        return self