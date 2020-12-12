from datetime import datetime
import CONSTANT
# print(datetime.datetime.timestamp(datetime.datetime.now()))   - Перевод в Unix час
# print(datetime.datetime.fromtimestamp(1607723431))            - Перевод в норм час


class User:
    def __init__(self, id, name, menu = CONSTANT.NAME_START_MENU,
                 date = datetime.timestamp(datetime.now()), money = 1000, gem = 1):
        self.id = id
        self.name = name
        self.menu = menu
        self.date = date
        self.money = money
        self.gem = gem

    def print(self):
        print(self.id, self.name, self.menu, self.date, self.money, self.gem)

    def get_string_gem(self):
        return ":gem:" + str(self.gem)
    def get_string_money(self):
        return ":moneybag:" + str(self.money)