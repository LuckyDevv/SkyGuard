import telebot
from telebot.types import KeyboardButton, InlineKeyboardButton


def get_start_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.add(KeyboardButton("Мой профиль ℹ️"))
    keyboard.add(KeyboardButton("Слить скаммера 😡"), KeyboardButton("Частые вопросы ❓"))
    keyboard.add(KeyboardButton("Гаранты ❤️‍🔥"), KeyboardButton("Стажёры 🌴"))
    keyboard.add(KeyboardButton("Статистика 📊"), KeyboardButton("Премиум 👑"))
    return keyboard


def get_profile_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔎 Проверить себя", callback_data="checkme"), InlineKeyboardButton("🎨 Тема проверки", callback_data="theme"))
    keyboard.add(InlineKeyboardButton("📣 Канал", callback_data="checkme"), InlineKeyboardButton("Страна", callback_data="theme"))
    keyboard.add(InlineKeyboardButton("❓ Как пользоваться ботом"))
    keyboard.add(InlineKeyboardButton("❤️ Своя картинка"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard


def get_merge_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Написать жалобу 📝", url="https://telegram.me/luckydevv"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard


def get_faq_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Кто такой гарант?", callback_data="faq1"), InlineKeyboardButton("Как найти гаранта?", callback_data="faq2"))
    keyboard.add(InlineKeyboardButton("Кто стать стажёром?", callback_data="faq3"), InlineKeyboardButton("Как стать гарантом?", callback_data="faq4"))
    keyboard.add(InlineKeyboardButton("Как слить скаммера?", callback_data="faq5"), InlineKeyboardButton("Когда набор стажёров?", callback_data="faq6"))
    keyboard.add(InlineKeyboardButton("Можно ли купить роль в базе?", callback_data="faq7"))
    keyboard.add(InlineKeyboardButton("Можно ли купить снятие из базы?", callback_data="faq8"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard


def get_stats_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Топ по сливам 🥷", callback_data="stats1"))
    keyboard.add(InlineKeyboardButton("Топ популярных 😸", callback_data="stats2"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard


def get_premium_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("12 месяцев - 999 ₽", callback_data="premium12m"))
    keyboard.add(InlineKeyboardButton("3 месяца - 499 ₽", callback_data="premium3m"))
    keyboard.add(InlineKeyboardButton("1 месяц - 199 ₽", callback_data="premium1m"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard
