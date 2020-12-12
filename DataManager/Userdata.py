import CONSTANT
import pandas as pd
from DataManager.User import User

class Userdata:
    def __init__(self):
        self.create_usersdata()
    def create_usersdata(self):
        data = pd.read_csv('content/data/Users.csv', encoding='cp1251', sep=',')
        self.users = []
        for i in range(len(data)):
            self.users.append(User(id = data['id'][i],
                                   name = data['name'][i],
                                   menu = data['menu'][i],
                                   date = data['date'][i],
                                   money = data['money'][i],
                                   gem = data['gem'][i]))

    def add_element(self, id, name, menu, date, money, gem): self.users.append(User(id, name, menu, date, money, gem))
    def add_new_user(self, id, name): self.users.append(User(id, name))

    def write_to_file(self):
        data = pd.DataFrame(
            {"id": [self.users[i].id for i in range(len(self.users))],
             "name": [self.users[i].name for i in range(len(self.users))],
             "menu": [self.users[i].menu for i in range(len(self.users))],
             "date": [self.users[i].date for i in range(len(self.users))],
             "money": [self.users[i].money for i in range(len(self.users))],
             "gem": [self.users[i].gem for i in range(len(self.users))]})
        data.to_csv('content/data/Users.csv', encoding='cp1251', index=False, header=True)

    def find_user(self, id):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    return self.users[i]
        #todo Генерувати виключення коли не знаходить користувача
    def find_user_statemenu(self, id): return self.find_user(id).menu
    def find_user_money(self, id): return self.find_user(id).money
    def set_user_money(self, id, money):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    self.users[i].money = money

    def change_state_menu(self, id, state):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    self.users[i].menu = state
