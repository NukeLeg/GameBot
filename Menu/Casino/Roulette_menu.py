import CONSTANT
from Menu.Menu import Menu
import telebot
import random

class Roulette_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        self.bets = {}
        self.etap = 0
        self.key_to_change = None
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_ROULETTE_MENU, regular_id=regular_id)

    def update(self, message):
        self.update_keyboard_start(message)
        self.update_inline(message)

    def update_keyboard_start(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True, row_width=4)
        for key in self.bets:
            keyboard.row("Ставка", key, str(self.bets[key]), "❌")
        keyboard.row('🚪 Назад', '❌ На головне меню')
        self.bot.send_message(self.regular_id, "Рулетка",  reply_markup = keyboard)
    def update_keyboard(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True, row_width=3)
        if len(self.bets)>0:
            keyboard.row("Ставка \n(Колір, числа..)", "Сума", "❌")
        sum = 0
        for key, i in zip(self.bets, range(len(self.bets))):
            keyboard.row(key, "{0}{1}\nСтавка {2}".format(CONSTANT.SYMBOL_MONEY, self.bets[key], i + 1), "❌ Ставка {}".format(i + 1))
            sum = sum + self.bets[key]
        if len(self.bets)>0:
            keyboard.row("Загальна сума", "{}{}".format(CONSTANT.SYMBOL_MONEY,sum), "❌")
        if len(self.bets) > 0:
            keyboard.row('💸Крутити')
        keyboard.row('🚪 Назад', '❌ На головне меню')
        self.bot.send_message(self.regular_id, "Ставки оновлені",  reply_markup = keyboard)
    def update_inline(self, message):
        image = open('content/images/roulette.jpg', 'rb')
        keyboard = telebot.types.InlineKeyboardMarkup(row_width = 6)
        keyboard.add(telebot.types.InlineKeyboardButton("🟥", callback_data="Red"),
                     telebot.types.InlineKeyboardButton("⬛", callback_data="Black"),
                     telebot.types.InlineKeyboardButton("EVEN", callback_data="EVEN"),
                     telebot.types.InlineKeyboardButton("ODD", callback_data="ODD"),
                     telebot.types.InlineKeyboardButton("1-18", callback_data="1-18"),
                     telebot.types.InlineKeyboardButton("19-36", callback_data="19-36"))

        keyboard.add(telebot.types.InlineKeyboardButton("dozer[1:12]", callback_data="d1"),
                     telebot.types.InlineKeyboardButton("dozer[13:24]", callback_data="d2"),
                     telebot.types.InlineKeyboardButton("dozer[25:36]", callback_data="d3"))
        keyboard.add(telebot.types.InlineKeyboardButton("column[1]", callback_data="c1"),
                     telebot.types.InlineKeyboardButton("column[2]", callback_data="c2"),
                     telebot.types.InlineKeyboardButton("column[3]", callback_data="c3"))
        keyboard.add(telebot.types.InlineKeyboardButton("1-6", callback_data="1-6"),
                     telebot.types.InlineKeyboardButton("7-12", callback_data="7-12"),
                     telebot.types.InlineKeyboardButton("13-18", callback_data="13-18"),
                     telebot.types.InlineKeyboardButton("19-24", callback_data="19-24"),
                     telebot.types.InlineKeyboardButton("25-30", callback_data="25-30"),
                     telebot.types.InlineKeyboardButton("31-36", callback_data="31-36"))
        keyboard.add(telebot.types.InlineKeyboardButton("1-3", callback_data="1-3"),
                     telebot.types.InlineKeyboardButton("4-6", callback_data="4-6"),
                     telebot.types.InlineKeyboardButton("7-9", callback_data="7-9"),
                     telebot.types.InlineKeyboardButton("10-12", callback_data="10-12"),
                     telebot.types.InlineKeyboardButton("13-15", callback_data="13-15"),
                     telebot.types.InlineKeyboardButton("16-18", callback_data="16-18"))
        keyboard.add(telebot.types.InlineKeyboardButton("19-21", callback_data="19-21"),
                     telebot.types.InlineKeyboardButton("22-24", callback_data="22-24"),
                     telebot.types.InlineKeyboardButton("25-27", callback_data="25-27"),
                     telebot.types.InlineKeyboardButton("28-30", callback_data="28-30"),
                     telebot.types.InlineKeyboardButton("31-33", callback_data="31-33"),
                     telebot.types.InlineKeyboardButton("34-36", callback_data="34-36"))
        keyboard.add(telebot.types.InlineKeyboardButton("0", callback_data="0"))
        keyboard.add(telebot.types.InlineKeyboardButton("1", callback_data="1"),
                     telebot.types.InlineKeyboardButton("2", callback_data="2"),
                     telebot.types.InlineKeyboardButton("3", callback_data="3"),
                     telebot.types.InlineKeyboardButton("4", callback_data="4"),
                     telebot.types.InlineKeyboardButton("5", callback_data="5"),
                     telebot.types.InlineKeyboardButton("6", callback_data="6"))
        keyboard.add(telebot.types.InlineKeyboardButton("7", callback_data="7"),
                     telebot.types.InlineKeyboardButton("8", callback_data="8"),
                     telebot.types.InlineKeyboardButton("9", callback_data="9"),
                     telebot.types.InlineKeyboardButton("10", callback_data="10"),
                     telebot.types.InlineKeyboardButton("11", callback_data="11"),
                     telebot.types.InlineKeyboardButton("12", callback_data="12"))
        keyboard.add(telebot.types.InlineKeyboardButton("13", callback_data="13"),
                     telebot.types.InlineKeyboardButton("14", callback_data="14"),
                     telebot.types.InlineKeyboardButton("15", callback_data="15"),
                     telebot.types.InlineKeyboardButton("16", callback_data="16"),
                     telebot.types.InlineKeyboardButton("17", callback_data="17"),
                     telebot.types.InlineKeyboardButton("18", callback_data="18"))
        keyboard.add(telebot.types.InlineKeyboardButton("19", callback_data="19"),
                     telebot.types.InlineKeyboardButton("20", callback_data="20"),
                     telebot.types.InlineKeyboardButton("21", callback_data="21"),
                     telebot.types.InlineKeyboardButton("22", callback_data="22"),
                     telebot.types.InlineKeyboardButton("23", callback_data="23"),
                     telebot.types.InlineKeyboardButton("24", callback_data="24"))
        keyboard.add(telebot.types.InlineKeyboardButton("25", callback_data="25"),
                     telebot.types.InlineKeyboardButton("26", callback_data="26"),
                     telebot.types.InlineKeyboardButton("27", callback_data="27"),
                     telebot.types.InlineKeyboardButton("28", callback_data="28"),
                     telebot.types.InlineKeyboardButton("29", callback_data="29"),
                     telebot.types.InlineKeyboardButton("30", callback_data="30"))
        keyboard.add(telebot.types.InlineKeyboardButton("31", callback_data="31"),
                     telebot.types.InlineKeyboardButton("32", callback_data="32"),
                     telebot.types.InlineKeyboardButton("33", callback_data="33"),
                     telebot.types.InlineKeyboardButton("34", callback_data="34"),
                     telebot.types.InlineKeyboardButton("35", callback_data="35"),
                     telebot.types.InlineKeyboardButton("36", callback_data="36"))
        self.bot.send_photo(self.regular_id, image, caption = 'На що будемо ставити? Виберіть із списку, або напишіть цифри самі через кому. Наприклад: \n2,3,5,6', reply_markup = keyboard)
    def update_need_to_change_money(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True, row_width=5)
        keyboard.row("10", "50", "100", "1000", "10000")
        keyboard.row("Відміна", "x2", "x5", "Скинути ставку")
        keyboard.row('🚪 Назад', '❌ На головне меню')
        self.bot.send_message(self.regular_id, "Впишіть нову суму ставки", reply_markup=keyboard)

    def press(self, message):
        if self.etap == 0: return self.press0(message)
        elif self.etap == 1: return self.press1(message)
        else: return self

    def press0(self, message):
        for key, i in zip(self.bets, range(len(self.bets))):
            if "❌ Ставка {}".format(i+1) in message.text:
                del self.bets[key]
                self.update_keyboard(message)
                break
            if "{0}{1}\nСтавка {2}".format(CONSTANT.SYMBOL_MONEY, self.bets[key], i+1) == message.text:
                self.update_need_to_change_money(message)
                self.key_to_change = key
                self.etap = 1
                return self

        if message.text == "❌":
            self.bets = {}
            self.bot.send_message(self.regular_id, "Скинуто всі ставки")
            self.update_inline(message)
            self.update_keyboard(message)
        elif "Сума" in message.text:
            sum = 0
            for key in self.bets:
                sum += self.bets[key]
            self.bot.send_message(self.regular_id, "Сума всіх ставок - {}{}".format(CONSTANT.SYMBOL_MONEY,sum))
        elif "Ставка" in message.text:
            info = "Всі ставки:\n"
            for key in self.bets:
                info += "Ставка {0}, сума {1}{2}\n".format(key, CONSTANT.SYMBOL_MONEY, self.bets[key])
            self.bot.send_message(self.regular_id, info)

        elif '💸Крутити' in message.text:
            self.spin_roulette(message)

        elif 'Назад' in message.text:
            from Menu.Casino.Casino_menu import Casino_menu
            menu = Casino_menu(message, self.userdata, self.bot)
            return menu
        elif 'На головне меню' in message.text:
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            return menu
        return self
    def press1(self, message):
        if '10' == message.text:
            self.etap = 0
            self.bets[self.key_to_change] = 10
            self.bot.send_message(self.regular_id, "Ставка стала 10")
            self.update_keyboard(message)
        elif '50' == message.text:
            self.etap = 0
            self.bets[self.key_to_change] = 50
            self.bot.send_message(self.regular_id, "Ставка стала 50")
            self.update_keyboard(message)
        elif '100' == message.text:
            self.etap = 0
            self.bets[self.key_to_change] = 100
            self.bot.send_message(self.regular_id, "Ставка стала 100")
            self.update_keyboard(message)
        elif '1000' == message.text:
            self.etap = 0
            self.bets[self.key_to_change] = 1000
            self.bot.send_message(self.regular_id, "Ставка стала 1000")
            self.update_keyboard(message)
        elif '10000' == message.text:
            self.etap = 0
            self.bets[self.key_to_change] = 10000
            self.bot.send_message(self.regular_id, "Ставка стала 10000")
            self.update_keyboard(message)
        elif 'Скинути ставку' in message.text:
            self.etap = 0
            del self.bets[self.key_to_change]
            self.key_to_change = None
            self.bot.send_message(self.regular_id, "Ставку скинуто")
            self.update_keyboard(message)
        elif 'x5' in message.text:
            self.etap = 0
            self.bets[self.key_to_change] = self.bets[self.key_to_change] * 5
            self.bot.send_message(self.regular_id, "Ставку збільшено впятеро")
            self.update_keyboard(message)
        elif 'x2' in message.text:
            self.etap = 0
            self.bets[self.key_to_change] = self.bets[self.key_to_change] * 2
            self.bot.send_message(self.regular_id, "Ставку подвоєно")
            self.update_keyboard(message)
        elif 'Відміна' in message.text:
            self.etap = 0
            self.bot.send_message(self.regular_id, "Нічого не змінено")
            self.update_keyboard(message)

        elif 'Назад' in message.text:
            from Menu.Casino.Casino_menu import Casino_menu
            menu = Casino_menu(message, self.userdata, self.bot)
            return menu
        elif 'На головне меню' in message.text:
            from Menu.General_menu import General_menu
            menu = General_menu(message, self.userdata, self.bot)
            return menu
        else:
            try:
                money = int(message.text)
                self.bets[self.key_to_change] = money
                self.bot.send_message(self.regular_id, "Ставку змінено до {}".format(money))
                self.etap = 0
                self.update_keyboard(message)
            except:
                self.bot.send_message(self.regular_id, "Некоректний ввод. Спробуйте ввести знову")
        return self
    def spin_roulette(self, message):
        random_number = random.randint(0, 36)
        color = "🟥"
        for i in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]: # red
            if random_number == i:
                color = "🟥"
        for i in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]: # black
            if random_number == i:
                color = "⬛"
        for i in [0]: # green
            if random_number == i:
                color = "️🟩"
        self.bot.send_message(self.regular_id, text='Випало __{1}{0}{1}__'.format(random_number, color), parse_mode= "MarkdownV2")



    def update_call(self, call):
        self.numbers = call.data
        self.bot.answer_callback_query(callback_query_id=call.id, text='Ставка додана, щоб змінити суму нажміть на значення в колонці "Сума"', show_alert=False)
        self.bets[call.data] = 1
        self.update_keyboard(None)
        # self.bot.send_message(call.message.chat.id, "+")
        #self.bot.answer_callback_query(call.id, text="Вибрано" + str(call), show_alert=True)
        #print(call)