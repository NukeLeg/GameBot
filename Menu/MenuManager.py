import CONSTANT
from Menu.About_menu import About_menu
from Menu.Add_menu import Add_menu
from Menu.Hello_menu import Hello_menu
from Menu.Help_menu import Help_menu
from Menu.Partnership_menu import Partnership_menu
from Menu.Start_menu import Start_menu
from Menu.Search_menu import Search_menu
from DataManager.Userdata import Userdata
import telebot

class MenuManager:
    def __init__(self, bot):
        self.user_menu = {}
        self.bot = bot
        self.userdata = Userdata()

    def start_new_user_menu(self, message):
        self.user_menu[message.chat.id] = Hello_menu(message, self.userdata, self.bot)

    def get_state_menu(self, message, id = None):
        if id == None:
            id = message.chat.id
        is_user_id = False
        for key in self.user_menu:
            if key == id:
                is_user_id = True

        if is_user_id == False:
            state = self.userdata.find_state_menu(id)
            self.bot.send_message(id, "Користувача знайдено, id: " + str(id))
            self.bot.send_message(id, "Загуржено із пам'яті стан меню: " + state)
            if state == CONSTANT.NAME_HELLO_MENU:
                self.user_menu[id] = Hello_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_START_MENU:
                self.user_menu[id] = Start_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_SEARCH_MENU:
                self.user_menu[id] = Search_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_PARTNERSHIP_MENU:
                self.user_menu[id] = Partnership_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_ADD_MENU:
                self.user_menu[id] = Add_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_HELP_MENU:
                self.user_menu[id] = Help_menu(message, self.userdata, self.bot)
            elif state == CONSTANT.NAME_ABOUT_MENU:
                self.user_menu[id] = About_menu(message, self.userdata, self.bot)
            else:
                self.user_menu[id] = Hello_menu(message, self.userdata, self.bot)


    def update_menu(self, message):
        new_user_menu = self.user_menu[message.chat.id].press(message)
        if new_user_menu != None:
            if new_user_menu != self.user_menu[message.chat.id]:
                self.user_menu[message.chat.id] = new_user_menu
                self.userdata.change_state_menu(message.chat.id, new_user_menu.state)
                self.userdata.write_to_file()
