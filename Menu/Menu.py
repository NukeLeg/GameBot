class Menu:
    def __init__(self, message, userdata, bot, state : str, regular_id = None):
        self.state = state
        self.userdata = userdata
        self.bot = bot
        if message != None:
            bot.send_message(message.chat.id, "bot змінив стан до: " + str(state))
            self.regular_id = message.chat.id
        if regular_id != None:
            self.regular_id = regular_id
        self.update(message)
    def update(self, message): pass
    def press(self, message): pass
    def info(self, call): pass