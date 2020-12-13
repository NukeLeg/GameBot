import CONSTANT
from Menu.Menu import Menu
import telebot

class Roulette_menu(Menu):
    def __init__(self, message, userdata, bot, regular_id=None):
        super().__init__(message=message, userdata=userdata, bot=bot, state=CONSTANT.NAME_ROULETTE_MENU, regular_id=regular_id)
        self.numbers = None
        self.money = 0

    def update(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚪 Назад', '❌ На головне меню')
        image = open('content/images/roulette.jpg', 'rb')
        self.bot.send_message(self.regular_id, "Рулетка")

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
        self.bot.send_photo(self.regular_id, image, caption = 'На що будемо ставити?', reply_markup = keyboard)

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