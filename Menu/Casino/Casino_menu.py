import CONSTANT
from Menu.Menu import Menu
import telebot

class Casino_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_CASINO_MENU, regular_id=regular_id)

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        self.lottery_ticket = self.userdata.find_user_lottery_ticket(self.regular_id)
        if self.lottery_ticket > 0:
            keyboard.row('Лотерея (' + CONSTANT.SYMBOL_LOTTERY_TICKET + str(self.lottery_ticket)+")")
        keyboard.row('Рулетка')
        keyboard.row('Автомат')
        keyboard.row('Назад')
        money = self.userdata.find_user_money(self.regular_id)
        self.bot.send_message(self.regular_id, 'У мене ' + CONSTANT.SYMBOL_MONEY + str(money), reply_markup = keyboard)

    def press(self, message):
        self.lottery_ticket = self.userdata.find_user_lottery_ticket(self.regular_id)
        if 'Лотерея' in message.text and self.lottery_ticket > 0:
            from Menu.Casino.Lottery_menu import Lottery_menu
            menu = Lottery_menu(message, self.userdata, self.bot)
            return menu
        elif message.text == 'Рулетка':
            from Menu.Casino.Rulette_menu import Rulette_menu
            menu = Rulette_menu(message, self.userdata, self.bot)
            return menu
        elif message.text == 'Автомат':
            from Menu.Casino.Automat_menu import Automat_menu
            menu = Automat_menu(message, self.userdata, self.bot)
            return menu
        elif message.text == 'Назад':
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            return menu
        return self