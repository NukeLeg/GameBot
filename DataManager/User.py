from datetime import datetime
import CONSTANT
# print(datetime.datetime.timestamp(datetime.datetime.now()))   - Перевод в Unix час
# print(datetime.datetime.fromtimestamp(1607723431))            - Перевод в норм час


class User:

    def __init__(self, id, name, menu = CONSTANT.NAME_START_MENU,
                 date_of_birthday = datetime.timestamp(datetime.now()), money = 100, gem = 1, lottery_ticket = 1,
                 lottery_last_get_ticket = datetime.timestamp(datetime.now())):
        self.id = id
        self.name = name
        self.menu = menu
        self.date_of_birthday = date_of_birthday
        self.money = money
        self.gem = gem
        self.lottery_ticket = lottery_ticket
        self.lottery_last_get_ticket = lottery_last_get_ticket

    def print(self):
        print(self.id, self.name, self.menu, self.date_of_birthday, self.money, self.gem)

    def check_new_lottery_ticket(self):
        if datetime.timestamp(datetime.now()) - self.lottery_last_get_ticket > CONSTANT.TIME_TO_NEW_LOTTERY_TICKET:
            self.lottery_ticket += 1
            self.lottery_last_get_ticket = datetime.timestamp(datetime.now())
            return True
        else:
            return False