import CONSTANT
from Menu.MenuManager import MenuManager
import telebot

bot = telebot.TeleBot(CONSTANT.BOT_TOKEN)
menu_manager = MenuManager(bot)

@bot.message_handler(commands = ['start'])
def welcome(message):
    menu_manager.start_new_user_menu(message)
    bot.send_message(message.chat.id, "Hello, GameBot greeting")

@bot.message_handler(commands = ['help'])
def welcome(message):
    bot.send_message(message.chat.id, "HELP command")

@bot.message_handler(content_types = ['text'])
def conversation(message):
    menu_manager.get_state_menu_if_user_is_not_in_operation_memory(message)
    menu_manager.update_menu(message)

bot.polling(none_stop=True)