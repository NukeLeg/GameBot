import CONSTANT
from Menu.Menu import Menu
import telebot

class Casino_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_CASINO_MENU, regular_id=regular_id)

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Рулетка')
        keyboard.row('Автомат')
        keyboard.row('Назад')
        money = self.userdata.find_user_money(self.regular_id)
        self.bot.send_message(self.regular_id, 'У мене 💰' + str(money), reply_markup = keyboard)

    def press(self, message):
        if message.text == 'Рулетка':
            from Menu.Casino.Rulette_menu import Rulette_menu
            menu = Rulette_menu(message, self.userdata, self.bot)
            return menu
        if message.text == 'Автомат':
            from Menu.Casino.Automat_menu import Automat_menu
            menu = Automat_menu(message, self.userdata, self.bot)
            return menu
        if message.text == 'Назад':
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            return menu
        return self