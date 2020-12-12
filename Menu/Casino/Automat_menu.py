import CONSTANT
from Menu.Menu import Menu
import telebot

class Automat_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        self.my_stavka = 0
        self.last_stavka = 0
        self.money = 0
        self.types_of_stavka = [1, 10, 100, 1000, 10000]
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_AUTOMAT_MENU, regular_id=regular_id)

    def update(self, message): # На початку
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Мала ставка', 'Середня ставка', 'Велика ставка')
        keyboard.row("Інфо", 'Назад🚪', 'На головне меню❌')
        self.money = self.userdata.find_user_money(self.regular_id)
        self.bot.send_message(self.regular_id, 'У Вас 💰' + str(self.money) + "\nЯка ставка?", reply_markup = keyboard)

    def update1(self, message): # Після ставки
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Мала ставка', 'Середня ставка', 'Велика ставка')
        keyboard.row('Крутити 🎰')
        keyboard.row("Інфо", 'Назад🚪', 'На головне меню❌')
        self.bot.send_message(self.regular_id, 'Ставка зроблена 💰' + str(self.my_stavka), reply_markup = keyboard)

    def update2(self, message): # Після кручення якщо хватає грошей
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
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
        elif message.text == "Крутити 🎰" and self.my_stavka > 0:
            self.spin()
            self.last_stavka = self.my_stavka
            self.my_stavka = 0
            if self.last_stavka<=self.money:
                self.update2(message)
            else:
                self.update(message)
        elif message.text == "Крутити знову 🎰" and self.last_stavka > 0 and self.money > self.last_stavka:
            self.my_stavka = self.last_stavka
            self.money = self.money - self.my_stavka
            self.spin()
            self.last_stavka = self.my_stavka
            self.my_stavka = 0
            if self.last_stavka <= self.money:
                self.update2(message)
            else:
                self.update(message)
        elif message.text == 'Інфо':
            self.bot.send_message(self.regular_id, '+')
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
    def write_money(self): self.userdata.set_user_money(self.regular_id, self.money)

    def spin(self):
        import random
        shaiba_number = 60
        elements = 5
        result = []
        string_result = ''
        for i in range(elements):
            result.append(random.randint(0, shaiba_number))
            string_result+=self.make_smile_from_number(result[i])
        prize = self.make_prize(result)
        self.money = self.money + prize
        self.bot.send_message(self.regular_id, ''+string_result)
        self.bot.send_message(self.regular_id, "Виграш 💰" + str(prize) + "  На рахунку 💰"+str(self.money))
        self.write_money()

    def make_smile_from_number(self, number):
        if number < 3: return "☠"   # Погане
        elif number < 6: return "💔" # Погане
        elif number < 9: return "💩" # Погане
        elif number < 14: return "🍎"   # Нейтральне
        elif number < 20: return "🍒"   # Нейтральне
        elif number < 26: return "🍌"   # Нейтральне
        elif number < 31: return "🥑"   # Нейтральне
        elif number < 36: return "🍕"   # Нейтральне
        elif number < 42: return "🐟"   # Нейтральне
        elif number < 47: return "🥥"  # Нейтральне
        elif number < 52: return "❤"   # Хороше
        elif number < 57: return "❄"   # Хороше
        elif number < 59: return "💎"  # Класне
        elif number == 59 : return "💯"  # Неймовірне
        elif number == 60: return "🎁"
        else: return ""
    def make_prize(self, result, stavka):
        score = 0

        return max(self.my_stavka * (score / 10), 0)

