from telebot import types


def create_help_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_about = types.InlineKeyboardButton(text='Обо мне', callback_data='/about')
    button_foto = types.InlineKeyboardButton(text='Фото', callback_data='/foto')
    button_voice = types.InlineKeyboardButton(text='Голосовые истории', callback_data='/voice')
    button_repo = types.InlineKeyboardButton(text='Ссылка на исходники бота', callback_data='/code-bot')
    button_secret = types.InlineKeyboardButton(text='Секретные функции', callback_data='/secret')
    keyboard.add(button_about, button_voice, button_foto, button_repo, button_secret)
    return keyboard


def create_down_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_down = types.InlineKeyboardButton(text='Главное меню', callback_data='/help')
    keyboard.add(button_down)
    return keyboard


def create_foto_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_foto1 = types.InlineKeyboardButton(text='Последнее селфи', callback_data='/last-foto')
    button_foto2 = types.InlineKeyboardButton(text='Фото с выпускного', callback_data='/schoole-foto')
    button_down = types.InlineKeyboardButton(text='Главное меню', callback_data='/help')
    keyboard.add(button_foto1, button_foto2, button_down)
    return keyboard


def create_secret_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_foto1 = types.InlineKeyboardButton(text='Ссылка на GitHub', callback_data='/gitHub')
    button_foto2 = types.InlineKeyboardButton(text='Ссылка на вк', callback_data='/vk')
    button_down = types.InlineKeyboardButton(text='Главное меню', callback_data='/help')
    keyboard.add(button_foto1, button_foto2, button_down)
    return keyboard
