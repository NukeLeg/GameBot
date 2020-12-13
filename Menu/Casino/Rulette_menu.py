import CONSTANT
from Menu.Menu import Menu
import telebot

class Rulette_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_RULETTE_MENU, regular_id=regular_id)

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚪 Назад', '❌ На головне меню')
        money = self.userdata.find_user_money(self.regular_id)
        self.bot.send_message(self.regular_id, '+', reply_markup = keyboard)

    def press(self, message):
        if 'Назад' in message.text:
            from Menu.Casino.Casino_menu import Casino_menu
            menu = Casino_menu(message, self.userdata, self.bot)
            return menu
        elif 'На головне меню' in message.text:
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            return menu
        return self