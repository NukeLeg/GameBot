import random

class Automat:
    number_of_types = 7

    horrible = ["☠"]
    bad = ["💔","💩"]
    normal = ['🍎','🍒','🍌','🥑','🍕',   '🐟','🍞','🥕','🍍','🌶']
    good = ["❤","❄",'🥥']
    wonderful =["💎"]
    great = ["💯"]
    perfect = ["🎁"]

    horrible_per = 3
    bad_per = 10
    normal_per = 16
    good_per = 12
    wonderful_per = 7
    great_per = 4
    perfect_per = 1

    def __init__(self):
        self.shaiba_number = \
            len(Automat.horrible) * Automat.horrible_per \
            + len(Automat.bad) * Automat.bad_per \
            + len(Automat.normal) * Automat.normal_per \
            + len(Automat.good) * Automat.good_per \
            + len(Automat.wonderful) * Automat.wonderful_per \
            + len(Automat.great) * Automat.great_per \
            + len(Automat.perfect) * Automat.perfect_per - 1
        self.elements = 5
        self.result_numbers = []
        self.rez = ''

    def spin_one_time(self):
        self.result_numbers = []
        self.rez = ''
        for i in range(self.elements):
            self.result_numbers.append(random.randint(0, self.shaiba_number))
            self.rez += self.make_smile_from_number(self.result_numbers[i])
    def make_smile_from_number(self, number):
        if   number < self.find_max_number_of_probability(0):
            return random.choice(Automat.horrible)
        elif number <  self.find_max_number_of_probability(1):
            return random.choice(Automat.bad)
        elif number < self.find_max_number_of_probability(2):
            return random.choice(Automat.normal)
        elif number < self.find_max_number_of_probability(3):
            return random.choice(Automat.good)
        elif number < self.find_max_number_of_probability(4):
            return random.choice(Automat.wonderful)
        elif number < self.find_max_number_of_probability(5):
            return random.choice(Automat.great)
        elif number < self.find_max_number_of_probability(6):
            return random.choice(Automat.perfect)
        else: return "⌂"
    def find_max_number_of_probability(self, number_of_type) -> int:
        to_return = len(Automat.horrible) * Automat.horrible_per
        if number_of_type == 0: return to_return
        to_return += len(Automat.bad) * Automat.bad_per
        if number_of_type == 1: return to_return
        to_return += len(Automat.normal) * Automat.normal_per
        if number_of_type == 2: return to_return
        to_return += len(Automat.good) * Automat.good_per
        if number_of_type == 3: return to_return
        to_return += len(Automat.wonderful) * Automat.wonderful_per
        if number_of_type == 4: return to_return
        to_return += len(Automat.great) * Automat.great_per
        if number_of_type == 5: return to_return
        to_return += len(Automat.perfect) * Automat.perfect_per
        if number_of_type == 6: return to_return
        return to_return

    def make_prize(self):
        score = 0
        for i in range(len(Automat.horrible)):
            count = self.get_count_of_symbol(Automat.horrible[i])
            score += -100 * count * count * count
        for i in range(len(Automat.bad)):
            count = self.get_count_of_symbol(Automat.bad[i])
            score += -5 * count * count
        for i in range(len(Automat.normal)):
            count = self.get_count_of_symbol(Automat.normal[i])
            score += 0 if count < 2 else count * count
        for i in range(len(Automat.good)):
            count = self.get_count_of_symbol(Automat.good[i])
            score += 2 * count * count
        for i in range(len(Automat.wonderful)):
            count = self.get_count_of_symbol(Automat.wonderful[i])
            score += 5 * count * count
        for i in range(len(Automat.great)):
            count = self.get_count_of_symbol(Automat.great[i])
            score += 25 * count * count * count
        for i in range(len(Automat.perfect)):
            count = self.get_count_of_symbol(Automat.perfect[i])
            score += 250 * count * count * count

        return max((score / 10), 0)

    def get_count_of_symbol(self, symbol):
        return self.rez.count(symbol)

    def info(self):
        string = '☠ - дуже погано\n'
        string += '💔,💩 - погано\n'
        string += '🍎,🍒,🍌,🥑,🍕,🐟,🍞,🥕,🍍,🌶 - звичайні\n'
        string += '❤,❄,🥥 - хороші\n'
        string += '💎,💯,🎁 - удачні\n'
        string += 'Чим більше однакових одного типу тим більший бонус\n'
        return string