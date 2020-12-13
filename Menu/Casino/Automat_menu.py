import CONSTANT
from Menu.Menu import Menu
from Menu.Casino.Automat import Automat
import telebot

class Automat_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        self.my_stavka = 0
        self.last_stavka = 0
        self.money = 0
        self.types_of_stavka = [1, 10, 100, 1000, 10000, 1000000]
        self.automat = Automat()
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_AUTOMAT_MENU, regular_id=regular_id)

    def update(self, message): # На початку
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        self.money = self.userdata.find_user_money(self.regular_id)
        if self.money + self.my_stavka > self.types_of_stavka[5]:
            keyboard.row('Нереальна ставка', 'Гіганська ставка')
        elif self.money + self.my_stavka < self.types_of_stavka[0]:
            keyboard.row('Піти в банк і взяти кредит щоб відігратися')
        elif self.money + self.my_stavka < self.types_of_stavka[1]:
            keyboard.row('Крихітна ставка')
        elif self.money + self.my_stavka > self.types_of_stavka[4]:
            keyboard.row('Гіганська ставка')
        keyboard.row('Мала ставка', 'Середня ставка', 'Велика ставка')
        keyboard.row("Інфо", 'Назад🚪', 'На головне меню❌')
        self.bot.send_message(self.regular_id, 'У Вас 💰' + str(self.money) + "\nЯка ставка?", reply_markup = keyboard)

    def update1(self, message): # Після ставки
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        if self.money + self.my_stavka > self.types_of_stavka[5]:
            keyboard.row('Нереальна ставка', 'Гіганська ставка')
        elif self.money + self.my_stavka < self.types_of_stavka[0]:
            keyboard.row('Піти в банк і взяти кредит щоб відігратися')
        elif self.money + self.my_stavka < self.types_of_stavka[1]:
            keyboard.row('Крихітна ставка')
        elif self.money + self.my_stavka > self.types_of_stavka[4]:
            keyboard.row('Гіганська ставка')
        keyboard.row('Мала ставка', 'Середня ставка', 'Велика ставка')
        keyboard.row('Крутити 🎰')
        keyboard.row("Інфо", 'Назад🚪', 'На головне меню❌')
        self.bot.send_message(self.regular_id, 'Ставка зроблена '+ CONSTANT.SYMBOL_MONEY + str(self.my_stavka) +
                              "\nНа рахунку "+ CONSTANT.SYMBOL_MONEY + str(self.money), reply_markup = keyboard)

    def update2(self, message): # Після кручення якщо хватає грошей
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        if self.money + self.my_stavka > self.types_of_stavka[5]:
            keyboard.row('Нереальна ставка', 'Гіганська ставка')
        elif self.money + self.my_stavka < self.types_of_stavka[0]:
            keyboard.row('Піти в банк і взяти кредит щоб відігратися')
        elif self.money + self.my_stavka < self.types_of_stavka[1]:
            keyboard.row('Крихітна ставка')
        elif self.money + self.my_stavka > self.types_of_stavka[4]:
            keyboard.row('Гіганська ставка')
        keyboard.row('Мала ставка', 'Середня ставка', 'Велика ставка')
        keyboard.row('Крутити знову 🎰')
        keyboard.row("Інфо", 'Назад🚪', 'На головне меню❌')
        self.bot.send_message(self.regular_id, 'Грати ще?', reply_markup = keyboard)

    def press(self, message):
        self.read_money()
        if message.text == 'Крихітна ставка' and self.money + self.my_stavka >= self.types_of_stavka[0]:
            self.money = self.money + self.my_stavka
            self.my_stavka = self.types_of_stavka[0]
            self.money = self.money - self.types_of_stavka[0]
            self.write_money()
            self.update1(message)
        elif message.text == 'Крихітна ставка' and self.money + self.my_stavka  < self.types_of_stavka[0]: self.not_enough()
        elif message.text == 'Мала ставка' and self.money + self.my_stavka  >= self.types_of_stavka[1]:
            self.money = self.money + self.my_stavka
            self.my_stavka = self.types_of_stavka[1]
            self.money = self.money - self.types_of_stavka[1]
            self.write_money()
            self.update1(message)
        elif message.text == 'Мала ставка' and self.money + self.my_stavka  < self.types_of_stavka[1]: self.not_enough()
        elif message.text == 'Середня ставка' and self.money + self.my_stavka  >= self.types_of_stavka[2]:
            self.money = self.money + self.my_stavka
            self.my_stavka = self.types_of_stavka[2]
            self.money = self.money - self.types_of_stavka[2]
            self.write_money()
            self.update1(message)
        elif message.text == 'Середня ставка' and self.money + self.my_stavka  < self.types_of_stavka[2]: self.not_enough()
        elif message.text == 'Велика ставка' and self.money + self.my_stavka  >= self.types_of_stavka[3]:
            self.money = self.money + self.my_stavka
            self.my_stavka = self.types_of_stavka[3]
            self.money = self.money - self.types_of_stavka[3]
            self.write_money()
            self.update1(message)
        elif message.text == 'Велика ставка' and self.money + self.my_stavka  < self.types_of_stavka[3]: self.not_enough()
        elif message.text == 'Гіганська ставка' and self.money + self.my_stavka  >= self.types_of_stavka[4]:
            self.money = self.money + self.my_stavka
            self.my_stavka = self.types_of_stavka[4]
            self.money = self.money - self.types_of_stavka[4]
            self.write_money()
            self.update1(message)
        elif message.text == 'Гіганська ставка' and self.money + self.my_stavka  < self.types_of_stavka[4]: self.not_enough()
        elif message.text == 'Нереальна ставка' and self.money + self.my_stavka  >= self.types_of_stavka[5]:
            self.money = self.money + self.my_stavka
            self.my_stavka = self.types_of_stavka[5]
            self.money = self.money - self.types_of_stavka[5]
            self.write_money()
            self.update1(message)
        elif message.text == 'Нереальна ставка' and self.money + self.my_stavka  < self.types_of_stavka[5]: self.not_enough()
        elif message.text == "Крутити 🎰" and self.my_stavka > 0:
            self.spin()
            self.last_stavka = self.my_stavka
            self.my_stavka = 0
            if self.last_stavka<=self.money:
                self.update2(message)
            else:
                self.update(message)
        elif message.text == "Крутити знову 🎰" and self.last_stavka > 0 and self.money >= self.last_stavka:
            self.my_stavka = self.last_stavka
            self.money = self.money - self.my_stavka
            self.bot.send_message(self.regular_id, 'Ставка зроблена '+ CONSTANT.SYMBOL_MONEY + str(self.my_stavka) +
                                  "\nНа рахунку "+ CONSTANT.SYMBOL_MONEY + str(self.money))
            self.spin()
            self.last_stavka = self.my_stavka
            self.my_stavka = 0
            if self.last_stavka <= self.money:
                self.update2(message)
            else:
                self.update(message)
        elif message.text == 'Інфо': self.bot.send_message(self.regular_id, self.automat.info())
        elif message.text == 'Піти в банк і взяти кредит щоб відігратися': self.bot.send_message(self.regular_id, "Поки банк не доступний, не побудували")
        elif message.text == 'Назад🚪':
            from Menu.Casino.Casino_menu import Casino_menu
            menu = Casino_menu(message, self.userdata, self.bot)
            self.money = self.money + self.my_stavka
            self.write_money()
            return menu
        elif message.text == 'На головне меню❌':
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            self.money = self.money + self.my_stavka
            self.write_money()
            return menu
        return self

    def not_enough(self): self.bot.send_message(self.regular_id, "Не вистачає")
    def read_money(self): self.money = self.userdata.find_user_money(self.regular_id)
    def write_money(self):
        self.userdata.set_user_money(self.regular_id, self.money)
        self.userdata.write_to_file()

    def spin(self):
        self.automat.spin_one_time()
        prize = int(self.automat.make_prize()*self.my_stavka)
        last_money = self.money
        self.money = self.money + prize
        self.bot.send_message(self.regular_id, '🎰       ' + self.automat.rez)
        self.bot.send_message(self.regular_id, "Виграш "+ CONSTANT.SYMBOL_MONEY + str(prize) +
                              "\nНа рахунку "+ CONSTANT.SYMBOL_MONEY + str(last_money) +
                              " \+ "+ CONSTANT.SYMBOL_MONEY + str(prize) +
                              " \= __*"+ CONSTANT.SYMBOL_MONEY + str(self.money) + "*__",
                              parse_mode= "MarkdownV2")
        self.write_money()



