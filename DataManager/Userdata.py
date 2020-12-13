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
                                   date_of_birthday= data['date_of_birthday'][i],
                                   money = data['money'][i],
                                   gem = data['gem'][i],
                                   lottery_ticket = data['lottery_ticket'][i],
                                   lottery_last_get_ticket=data['lottery_last_get_ticket'][i]))

    def add_element(self, id, name, menu, date_of_birthday, money, gem, lottery_last_get_ticket):
        self.users.append(User(id, name, menu, date_of_birthday, money, gem, lottery_last_get_ticket))
    def add_new_user(self, id, name): self.users.append(User(id, name))

    def write_to_file(self):
        data = pd.DataFrame(
            {"id": [self.users[i].id for i in range(len(self.users))],
             "name": [self.users[i].name for i in range(len(self.users))],
             "menu": [self.users[i].menu for i in range(len(self.users))],
             "date_of_birthday": [self.users[i].date_of_birthday for i in range(len(self.users))],
             "money": [self.users[i].money for i in range(len(self.users))],
             "gem": [self.users[i].gem for i in range(len(self.users))],
             "lottery_ticket": [self.users[i].lottery_ticket for i in range(len(self.users))],
             'lottery_last_get_ticket':[self.users[i].lottery_last_get_ticket for i in range(len(self.users))]})
        data.to_csv('content/data/Users.csv', encoding='cp1251', index=False, header=True)

    def is_exist_user(self, id):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    return True
        return False
    def find_user(self, id):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    return self.users[i]
        raise NoUserExist()
    def find_user_statemenu(self, id): return self.find_user(id).menu
    def find_user_money(self, id): return self.find_user(id).money
    def find_user_gem(self, id): return self.find_user(id).gem
    def find_user_lottery_ticket(self, id): return self.find_user(id).lottery_ticket

    def set_user_money(self, id, money):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    self.users[i].money = money

    def set_user_gem(self, id, gem):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    self.users[i].gem = gem

    def set_user_lottery_ticket(self, id, lottery_ticket):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    self.users[i].lottery_ticket = lottery_ticket

    def change_state_menu(self, id, state):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    self.users[i].menu = state

    def check_new_lottery_ticket(self, id):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    if self.users[i].check_new_lottery_ticket():
                        self.write_to_file()
                        return True
                    else:
                        return False

class NoUserExist(Exception):
    def __init__(self):
        super().__init__()