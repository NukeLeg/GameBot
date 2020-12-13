import CONSTANT
from Menu.Menu import Menu
import telebot
import random

class Lottery_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        self.lottery_ticket = 0
        self.money = 0
        self.gem = 0
        self.poll_task = None
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_LOTTERY_MENU, regular_id=regular_id)

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        self.lottery_ticket = self.userdata.find_user_lottery_ticket(self.regular_id)
        if self.lottery_ticket > 0:
            keyboard.row('Використати один білет ('+CONSTANT.SYMBOL_LOTTERY_TICKET+str(self.lottery_ticket)+")")
        keyboard.row('🚪 Назад', '❌ На головне меню')
        if self.lottery_ticket > 0:
            self.bot.send_message(self.regular_id, "Випробувати удачу?", reply_markup = keyboard)
        else:
            self.bot.send_message(self.regular_id, "Квитки закінчилися", reply_markup = keyboard)

    def update1(self, message): # message = None
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        self.lottery_ticket = self.userdata.find_user_lottery_ticket(self.regular_id)
        if self.lottery_ticket > 0:
            keyboard.row('Використати один білет ('+CONSTANT.SYMBOL_LOTTERY_TICKET+str(self.lottery_ticket)+")")
        keyboard.row('🚪 Назад', '❌ На головне меню')
        if self.lottery_ticket > 0:
            self.bot.send_message(self.regular_id, "...", reply_markup = keyboard)
        else:
            self.bot.send_message(self.regular_id, "Квитки закінчилися", reply_markup = keyboard)

    def press(self, message):
        self.lottery_ticket = self.userdata.find_user_lottery_ticket(self.regular_id)
        if 'Використати один білет' in message.text and self.lottery_ticket > 0:
            self.poll_task = self.bot.send_poll(self.regular_id, "Виберіть одне із: ", ["коробка", 'бутилка', 'ящік', 'носок', "мішок", "пачка"], is_anonymous=False)
            self.change_and_write(lottery_ticket=-1)
            self.update1(message)
        elif 'Назад' in message.text:
            if self.poll_task != None:
                self.bot.stop_poll(self.regular_id, self.poll_task.message_id)
            from Menu.Casino.Casino_menu import Casino_menu
            menu = Casino_menu(message, self.userdata, self.bot)
            return menu
        elif 'На головне меню' in message.text:
            if self.poll_task != None:
                self.bot.stop_poll(self.regular_id, self.poll_task.message_id)
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            return menu
        return self

    def read_resources(self):
        self.money = self.userdata.find_user_money(self.regular_id)
        self.gem = self.userdata.find_user_gem(self.regular_id)
        self.lottery_ticket = self.userdata.find_user_lottery_ticket(self.regular_id)
    def write_resources(self):
        self.userdata.set_user_money(self.regular_id, self.money)
        self.userdata.set_user_gem(self.regular_id, self.gem)
        self.userdata.set_user_lottery_ticket(self.regular_id, self.lottery_ticket)
        self.userdata.write_to_file()
    def change_and_write(self, money = 0, gem = 0, lottery_ticket = 0):
        self.read_resources()
        self.money += money
        self.gem += gem
        self.lottery_ticket += lottery_ticket
        self.write_resources()
    def add_random_money(self, start = 1, finish = 10):
        to_add = random.randint(start,finish)
        to_add = random.choice([1,5,10,20,50,50,50,75,100,500,1000])
        self.change_and_write(money = to_add)
        return CONSTANT.SYMBOL_MONEY + str(to_add)
    def add_random_gem(self, start = 1, finish = 2):
        to_add = random.randint(start,finish)
        self.change_and_write(gem = to_add)
        return CONSTANT.SYMBOL_GEM + str(to_add)
    def add_random_lottery_ticket(self, start = 1, finish = 2):
        to_add = random.randint(start,finish)
        self.change_and_write(lottery_ticket = to_add)
        return CONSTANT.SYMBOL_LOTTERY_TICKET + str(to_add)

    def poll(self, quiz_answer):
        if quiz_answer.options_ids[0] == 0:
            add_random_res = random.choice([self.add_random_money, self.add_random_gem, self.add_random_lottery_ticket])
            self.bot.send_message(self.regular_id, 'У коробці було ' + add_random_res())
        elif quiz_answer.options_ids[0] == 1:
            add_random_res = random.choice([self.add_random_money, self.add_random_gem, self.add_random_lottery_ticket])
            self.bot.send_message(self.regular_id, 'У бутилці було' + add_random_res())
        elif quiz_answer.options_ids[0] == 2:
            add_random_res = random.choice([self.add_random_money, self.add_random_gem, self.add_random_lottery_ticket])
            self.bot.send_message(self.regular_id, 'В ящику було' + add_random_res())
        elif quiz_answer.options_ids[0] == 3:
            add_random_res = random.choice([self.add_random_money, self.add_random_gem, self.add_random_lottery_ticket])
            self.bot.send_message(self.regular_id, 'У носку було' + add_random_res())
        elif quiz_answer.options_ids[0] == 4:
            add_random_res = random.choice([self.add_random_money, self.add_random_gem, self.add_random_lottery_ticket])
            self.bot.send_message(self.regular_id, 'У мішку було' + add_random_res())
        elif quiz_answer.options_ids[0] == 5:
            add_random_res = random.choice([self.add_random_money, self.add_random_gem, self.add_random_lottery_ticket])
            self.bot.send_message(self.regular_id, 'У пачці було' + add_random_res())
        elif quiz_answer.options_ids[0] == 6:
            add_random_res = random.choice([self.add_random_money, self.add_random_gem, self.add_random_lottery_ticket])
            self.bot.send_message(self.regular_id, 'У коробці було' + add_random_res())
        else:
            self.bot.send_message(self.regular_id, 'Чітерство')
        self.update1(None)