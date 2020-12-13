import CONSTANT
from Menu.Menu import Menu
import telebot


class General_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_GENERAL_MENU, regular_id = regular_id)

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Профіль')
        lottery_ticket = self.userdata.find_user_lottery_ticket(self.regular_id)
        if lottery_ticket > 0:
            keyboard.row('Казино (' +CONSTANT.SYMBOL_LOTTERY_TICKET+ str(lottery_ticket)+")")
        else:
            keyboard.row('Казино')
        self.bot.send_message(self.regular_id, 'Головне меню', reply_markup=keyboard)
        if self.userdata.check_new_lottery_ticket(self.regular_id):
            self.bot.send_message(self.regular_id, 'Ви отримали лотерейний квиток!! ' + CONSTANT.SYMBOL_LOTTERY_TICKET, reply_markup=keyboard)

    def press(self, message):
        if 'Профіль' in message.text:
            from Menu.Home.Home_menu import Home_menu
            menu = Home_menu(message, self.userdata, self.bot)
            return menu
        if 'Казино' in message.text:
            from Menu.Casino.Casino_menu import Casino_menu
            menu = Casino_menu(message, self.userdata, self.bot)
            return menu
        return self