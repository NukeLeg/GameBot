import CONSTANT
from Menu.Menu import Menu
import telebot

class Hello_menu(Menu): # Початкове меню
    def __init__(self, message, userdata,  bot, regular_id = None):
        super().__init__(message = message, userdata = userdata, bot = bot, state = CONSTANT.NAME_HELLO_MENU, regular_id = regular_id)
    def update(self, message):
        startinfo = 'Hello '+ (message.from_user.first_name if message != None else "")
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Начать')
        self.bot.send_message(self.regular_id, startinfo, reply_markup = keyboard)
    def press(self, message):
        if message.text == 'Начать':
            from Menu.Start_menu import Start_menu
            menu = Start_menu(message, self.userdata, self.bot)
            return menu
        return self