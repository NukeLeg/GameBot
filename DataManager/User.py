class User:
    def __init__(self, id, name, menu):
        self.id = id
        self.name = name
        self.menu = menu

    def print(self):
        print(self.id, self.name, self.menu)