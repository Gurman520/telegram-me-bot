import text as t
import keyboards as kb


def main_menu_handler(bot, message):
    print("Telegram bot", "Main_menu_handler")
    keyboard = kb.create_main_keyboard()
    chat_id = message.chat.id
    bot.send_message(chat_id, t.main_menu, reply_markup=keyboard)


def handle_start(bot, message):
    print("Telegram bot", "Handler_start")
    user_id = message.chat.id
    bot.send_message(user_id, t.start)


def about_handler(bot, message):
    print("Telegram bot", "About_handler")
    keyboard = kb.create_down_keyboard()
    chat_id = message.chat.id
    bot.send_message(chat_id, t.about, reply_markup=keyboard)


def foto_handler(bot, message):
    print("Telegram bot", "Foto_handler")
    keyboard = kb.create_foto_keyboard()
    chat_id = message.chat.id
    bot.send_message(chat_id, t.foto, reply_markup=keyboard)
   

def foto_selfi_handler(bot, message):
    print("Telegram bot", "Selfi_handler")
    keyboard = kb.create_down_keyboard()
    photo = open('media/foto/selfi.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=t.selfi_foto, reply_markup=keyboard)


def foto_old_handler(bot, message):
    print("Telegram bot", "Foto_old_handler")
    keyboard = kb.create_down_keyboard()
    photo = open('media/foto/old.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=t.old_foto, reply_markup=keyboard)


def code_bot_handler(bot, message):
    print("Telegram bot", "Code_bot_handler")
    keyboard = kb.create_down_keyboard()
    chat_id = message.chat.id
    bot.send_message(chat_id, t.code_bot, reply_markup=keyboard)


def secret_handler(bot, message):
    print("Telegram bot", "Secret_handler")
    keyboard = kb.create_secret_keyboard()
    chat_id = message.chat.id
    bot.send_message(chat_id, t.secret_menu, reply_markup=keyboard)


def gitHub_handler(bot, message):
    print("Telegram bot", "GitHub_handler")
    keyboard = kb.create_down_keyboard()
    chat_id = message.chat.id
    bot.send_message(chat_id, t.github, reply_markup=keyboard)


def vk_handler(bot, message):
    print("Telegram bot", "Vk_handler")
    keyboard = kb.create_down_keyboard()
    chat_id = message.chat.id
    bot.send_message(chat_id, t.vk, reply_markup=keyboard)


def voice_handler(bot, message):
    print("Telegram bot", "Voice_handler")
    keyboard = kb.create_voice_keyboard()
    chat_id = message.chat.id
    bot.send_message(chat_id, t, reply_markup=keyboard)


def article_handler(bot, message):
    print("Telegram bot", "Article_handler")
    keyboard = kb.create_down_keyboard()
    chat_id = message.chat.id
    try:
        f = open("media/documents/article.txt", 'r', encoding='utf-8')
    except OSError:
        bot.send_message(chat_id, t.error, reply_markup=keyboard)
        return 
    text = f.read()
    bot.send_message(chat_id, text, reply_markup=keyboard)


def help_handler(bot, message):
    keyboard = kb.create_main_keyboard()
    print("Telegram bot", "Help_handler")
    chat_id = message.chat.id
    bot.send_message(chat_id, t.help, reply_markup=keyboard)
    

def unknown_command_handler(bot, message):
    user_id = message.chat.id
    bot.send_message(
        user_id, "Упс... Кажется такой команды нету, напиши /help, чтобы увидеть список команд")