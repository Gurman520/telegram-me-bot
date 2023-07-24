from telebot import types


def create_main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_about = types.InlineKeyboardButton(text='О моем создателе', callback_data='/about')
    button_text = types.InlineKeyboardButton(text='Пост', callback_data='/article')
    button_foto = types.InlineKeyboardButton(text='Фото', callback_data='/foto')
    button_voice = types.InlineKeyboardButton(text='Голосовые истории', callback_data='/voice')
    button_repo = types.InlineKeyboardButton(text='Ссылка на исходники бота', callback_data='/code-bot')
    # button_secret = types.InlineKeyboardButton(text='Секретные функции', callback_data='/secret')
    # keyboard.add(button_about, button_text, button_voice, button_foto, button_repo)
    keyboard.row(button_about, button_text, button_foto)
    keyboard.row(button_voice, button_repo)
    return keyboard


def create_down_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_down = types.InlineKeyboardButton(text='Главное меню', callback_data='/main')
    keyboard.add(button_down)
    return keyboard


def create_foto_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_foto1 = types.InlineKeyboardButton(text='Последнее селфи', callback_data='/last-foto')
    button_foto2 = types.InlineKeyboardButton(text='Фото с выпускного', callback_data='/schoole-foto')
    button_down = types.InlineKeyboardButton(text='Главное меню', callback_data='/main')
    keyboard.add(button_foto1, button_foto2, button_down)
    return keyboard


def create_secret_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_foto1 = types.InlineKeyboardButton(text='Ссылка на GitHub', callback_data='/gitHub')
    button_foto2 = types.InlineKeyboardButton(text='Ссылка на вк', callback_data='/vk')
    button_down = types.InlineKeyboardButton(text='Главное меню', callback_data='/main')
    keyboard.add(button_foto1, button_foto2, button_down)
    return keyboard


def create_voice_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_gpt = types.InlineKeyboardButton(text='Что такое GPT', callback_data='/gpt')
    button_sql = types.InlineKeyboardButton(text='Различие SQL и NoSQL', callback_data='/sql_vs_nosql')
    button_love = types.InlineKeyboardButton(text='История первой любви U+1F495', callback_data='/f_love')
    button_down = types.InlineKeyboardButton(text='Главное меню', callback_data='/main')
    keyboard.add(button_gpt, button_sql, button_love, button_down)
    return keyboard
