import CONSTANT
from Menu.Menu import Menu
import telebot

class Search_menu(Menu):  # Поиск
    def __init__(self, message, userdata, bot, regular_id = None):
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_SEARCH_MENU, regular_id = regular_id)
        self.etap = etap
        self.result = None

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Как искать?')
        keyboard.row('На головне меню')
        message_sent = self.bot.send_message(self.regular_id, "...", reply_markup=keyboard)
        self.bot.delete_message(self.regular_id, message_id = message_sent.id)

    def press(self, message):
        return self