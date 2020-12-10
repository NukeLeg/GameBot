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
            self.users.append(User(id = data['id'][i], name = data['name'][i], menu = data['menu'][i]))

    def add_element(self, id_vvod, name_vvod, menu_vvod):
        user = User(id_vvod, name_vvod, menu_vvod)
        self.users.append(user)

    def write_to_file(self):
        data = pd.DataFrame(
            {"id": [self.users[i].id for i in range(len(self.users))],
             "name": [self.users[i].name for i in range(len(self.users))],
             "menu": [self.users[i].menu for i in range(len(self.users))]})
        data.to_csv('content/data/Users.csv', encoding='cp1251', index=False, header=True)

    ''' Перевіряє чи існує id користувача, якщо його немає то додає в базу даних'''
    def check_is_the_same_id(self, id, name, menu):
        if len(self.users) == 0:
            self.users.append(User(id,name,menu))
        else:
            is_same = False
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    is_same = True
                    break
            if is_same == False:
                self.users.append(User(id, name, menu))

    def find_user(self, id):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    return self.users[i]

    def find_state_menu(self, id):
        return self.find_user(id).menu

    def change_state_menu(self, id, state):
        if len(self.users) == 0:
            pass  #todo Обробити таке виключення
        else:
            for i in range(len(self.users)):
                if self.users[i].id == id:
                    self.users[i].menu = state

    def change_state_menu_to_search(self, id):
        self.change_state_menu(id, CONSTANT.NAME_SEARCH_MENU)

    def print(self):
        for user in self.users:
            user.print()