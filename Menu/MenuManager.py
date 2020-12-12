import CONSTANT
from Menu.Help_menu import Help_menu
from Menu.Start_menu import Start_menu
from Menu.General_menu import General_menu
from Menu.Home.Home_menu import Home_menu
from Menu.Casino.Casino_menu import Casino_menu
from Menu.Casino.Automat_menu import Automat_menu
from Menu.Casino.Rulette_menu import Rulette_menu
from DataManager.Userdata import Userdata
import telebot

class MenuManager:
    def __init__(self, bot):
        self.user_menu = {}
        self.bot = bot
        self.userdata = Userdata()

    def start_new_user_menu(self, message):
        if self.check_is_exist(message):
            self.add_new_user_to_database(message)
            self.add_menu_to_new_user(message)
    def check_is_exist(self, message):
        return False
    def add_new_user_to_database(self, message):
        pass # todo add new user to database
    def add_menu_to_new_user(self, message):
        self.user_menu[message.chat.id] = Start_menu(message, self.userdata, self.bot) #todo add menu to operation memory


    def update_menu(self, message):
        self.get_state_menu_if_user_is_not_in_operation_memory(message)
        self.update_menu_state(message)
    def get_state_menu_if_user_is_not_in_operation_memory(self, message):
        id = message.chat.id
        is_user_id = False
        for key in self.user_menu:
            if key == id:
                is_user_id = True
        if is_user_id == False:
            state = self.userdata.find_user_statemenu(id)
            self.bot.send_message(id, "Користувача знайдено, id: " + str(id))
            self.bot.send_message(id, "Загуржено із пам'яті стан меню: " + state)
            if state == CONSTANT.NAME_START_MENU:
                self.user_menu[id] = Start_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_HELP_MENU:
                self.user_menu[id] = Help_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_GENERAL_MENU:
                self.user_menu[id] = General_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_HOME_MENU:
                self.user_menu[id] = Home_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_CASINO_MENU:
                self.user_menu[id] = Casino_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_AUTOMAT_MENU:
                self.user_menu[id] = Automat_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_RULETTE_MENU:
                self.user_menu[id] = Rulette_menu(message, self.userdata, self.bot)
            else:
                self.user_menu[id] = General_menu(message, self.userdata, self.bot)
    def update_menu_state(self, message):
        new_user_menu = self.user_menu[message.chat.id].press(message)
        if new_user_menu != None and new_user_menu != self.user_menu[message.chat.id]:
            self.user_menu[message.chat.id] = new_user_menu
            self.userdata.change_state_menu(message.chat.id, new_user_menu.state)
            self.userdata.write_to_file()



