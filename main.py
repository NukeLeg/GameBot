import CONSTANT
from Menu.MenuManager import MenuManager
import telebot

bot = telebot.TeleBot(CONSTANT.BOT_TOKEN)
menu_manager = MenuManager(bot)

@bot.message_handler(commands = ['start'])
def welcome(message):
    menu_manager.start_new_user_menu(message)
    bot.send_message(message.chat.id, "Hello, GameBot greeting")

@bot.message_handler(commands = ['adv'])
def adver(message):
    menu_manager.advertisement()

@bot.callback_query_handler(func = lambda call: True)
def query_handler(call):
    menu_manager.update_call(call)

@bot.message_handler(content_types = ['text'])
def conversation(message):
    menu_manager.get_state_menu(message)
    menu_manager.update_menu(message)


bot.polling(none_stop=True)