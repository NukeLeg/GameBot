import CONSTANT
from Menu.MenuManager import MenuManager
import telebot

bot = telebot.TeleBot(CONSTANT.BOT_TOKEN)
menu_manager = MenuManager(bot)

@bot.message_handler(commands = ['start'])
def welcome(message):
    menu_manager.start_new_user_menu(message)

@bot.message_handler(commands = ['help'])
def welcome(message):
    bot.send_message(message.chat.id, "HELP command")

@bot.message_handler(content_types = ['text'])
def conversation(message):
    menu_manager.update_menu(message)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    menu_manager.update_call(call)

@bot.poll_answer_handler()
def poll_message(quiz_answer):
    menu_manager.update_poll(quiz_answer)

bot.polling(none_stop=True)