import CONSTANT
from Menu.Menu import Menu
import telebot

class About_menu(Menu): # О проекте
    def __init__(self, message, userdata, bot, regular_id = None):
        super().__init__(message = message, userdata = userdata,  bot = bot, state = CONSTANT.NAME_ABOUT_MENU, regular_id = regular_id)
    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Назад')
        self.bot.send_message(self.regular_id, '##########\n#############\n###########\nSome information', reply_markup = keyboard)
    def press(self, message):
        if message.text == 'Назад':
            from Menu.Start_menu import Start_menu
            menu = Start_menu(message, self.userdata, self.gravedata, self.bot)
            return menu
        return self