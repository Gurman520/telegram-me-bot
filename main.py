from telebot import TeleBot
import handler as hd


TOKEN = '' # токен доступа к боту
bot = TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "/start":
        hd.handle_start(bot, message)
    elif message.text == "/help":
        hd.help_handler(bot, message)
    else:
        hd.unknown_command_handler(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "/about":
        hd.about_handler(bot, call.message)
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
    elif call.data == "/secret":
        hd.secret_handler(bot, call.message)
    elif call.data == "/gitHub":
        hd.gitHub_handler(bot, call.message)
    elif call.data == "/vk":
        hd.vk_handler(bot, call.message)
    





print("Start bot")
bot.polling()
