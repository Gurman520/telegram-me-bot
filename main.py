import os
from telebot import TeleBot
import handler as hd
from dotenv import load_dotenv


dotenv_path = os.path.join('env_bot.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


TOKEN = os.getenv("TOKEN")
if TOKEN == None:
    exit()
bot = TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "/start":
        hd.handle_start(bot, message)
    elif message.text == "/help":
        hd.help_handler(bot, message)
    elif message.text == "/secret":
        hd.secret_handler(bot, message)
    else:
        hd.unknown_command_handler(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "/about":
        hd.about_handler(bot, call.message)
    elif call.data == "/main":
        hd.main_menu_handler(bot, call.message)
    elif call.data == "/help":
        hd.help_handler(bot, call.message)
    elif call.data == "/foto":
        hd.foto_handler(bot, call.message)
    elif call.data == "/last-foto":
        hd.foto_selfi_handler(bot, call.message)
    elif call.data == "/schoole-foto":
        hd.foto_old_handler(bot, call.message)
    elif call.data == "/code-bot":
        hd.code_bot_handler(bot, call.message)
    elif call.data == "/gitHub":
        hd.gitHub_handler(bot, call.message)
    elif call.data == "/vk":
        hd.vk_handler(bot, call.message)
    elif call.data == "/article":
        hd.article_handler(bot, call.message)
    elif call.data == "/voice":
        hd.voice_handler(bot, call.message)
    elif call.data == "/f_love":
        hd.first_love_handler(bot, call.message)
    elif call.data == "/sql_vs_nosql":
        hd.sql_handler(bot, call.message)
    elif call.data == "/gpt":
        hd.gpt_handler(bot, call.message)
    elif call.data == "/sert":
        hd.cert_handler(bot, call.message)



print("Start bot")
bot.polling()
