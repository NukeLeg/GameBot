import random

class Character:
    def __init__(self, health, damage):
        self.health_max = health
        self.health = health
        self.damage = damage
        self.is_alive = True
    def get_damage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.is_alive = False

    def life_percent(self):
        return self.health/self.health_max

    def make_damage(self):
        if self.is_alive:
            return random.randint(self.damage[0], self.damage[1])
        else:
            return 0
