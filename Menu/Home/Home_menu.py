import CONSTANT
from Menu.Menu import Menu
import telebot

class Home_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_HOME_MENU, regular_id=regular_id)

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Назад')
        money = self.userdata.find_user_money(self.regular_id)
        gem = self.userdata.find_user_gem(self.regular_id)
        lottery_ticket = self.userdata.find_user_lottery_ticket(self.regular_id)
        self.bot.send_message(self.regular_id, 'У мене \n' + CONSTANT.SYMBOL_MONEY + str(money)
                              + '\n' + CONSTANT.SYMBOL_GEM + str(gem)
                              + "\n"+ CONSTANT.SYMBOL_LOTTERY_TICKET + str(lottery_ticket), reply_markup = keyboard)

    def press(self, message):
        if message.text == 'Назад':
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            return menu
        return self