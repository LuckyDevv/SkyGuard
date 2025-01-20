import telebot
from telebot.types import KeyboardButton, InlineKeyboardButton


def get_start_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add(KeyboardButton("Мой профиль ℹ️"))
    keyboard.add(KeyboardButton("Слить скаммера 😡"), KeyboardButton("Частые вопросы ❓"))
    keyboard.add(KeyboardButton("Гаранты ❤️‍🔥"), KeyboardButton("Стажёры 🌴"))
    keyboard.add(KeyboardButton("Статистика 📊"), KeyboardButton("Премиум 👑"))
    return keyboard


def get_profile_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔎 Проверить себя", callback_data="checkme"), InlineKeyboardButton("🎨 Тема проверки", callback_data="theme"))
    keyboard.add(InlineKeyboardButton("📣 Канал", callback_data="channel"), InlineKeyboardButton("Страна", callback_data="country"))
    keyboard.add(InlineKeyboardButton("❓ Как пользоваться ботом", callback_data="faq"))
    keyboard.add(InlineKeyboardButton("❤️ Своя картинка", callback_data="custom-image"))
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
    keyboard.add(InlineKeyboardButton("Как стать стажёром?", callback_data="faq3"), InlineKeyboardButton("Как стать гарантом?", callback_data="faq4"))
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


def get_stats1_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Статистика 📊", callback_data="stats0"))
    keyboard.add(InlineKeyboardButton("Топ популярных 😸", callback_data="stats2"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard


def get_stats2_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Статистика 📊", callback_data="stats0"))
    keyboard.add(InlineKeyboardButton("Топ по сливам 🥷", callback_data="stats1"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard


def get_premium_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("12 месяцев - 999 ₽", callback_data="premium12m"))
    keyboard.add(InlineKeyboardButton("3 месяца - 499 ₽", callback_data="premium3m"))
    keyboard.add(InlineKeyboardButton("1 месяц - 199 ₽", callback_data="premium1m"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard


def get_faq_cancel_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Вернуться ↩️", callback_data="faq0"))
    return keyboard


def get_faq2_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Добавить в чат", url="https://t.me/sasd_test_bot?startgroup=newgroup&admin=manage_chat+delete_messages+restrict_members+invite_users+restrict_members+change_info+pin_messages+manage_video_chats"))
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    keyboard.add(InlineKeyboardButton("Назад", callback_data="profile"))
    return keyboard


def get_premium_cancel_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Вернуться ↩️", callback_data="premium0"))
    return keyboard


def get_custom_image_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Отмена", callback_data="custom-image-cancel"))
    return keyboard


def get_channel_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Отмена", callback_data="channel-cancel"))
    return keyboard


def get_list_keyboard(users):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    if users is not None:
        for i in range(0, len(users), 2):
            row = []
            if i < len(users):
                username, first_name = users[i]
                if username != "":
                    row.append(InlineKeyboardButton(first_name, url="https://t.me/" + username))
                else:
                    row.append(InlineKeyboardButton(first_name, callback_data=username))
            if i + 1 < len(users):
                username, first_name = users[i + 1]
                if username != "":
                    row.append(InlineKeyboardButton(first_name, url="https://t.me/" + username))
                else:
                    row.append(InlineKeyboardButton(first_name, callback_data=username))
            keyboard.add(*row)
    keyboard.add(InlineKeyboardButton("Скрыть", callback_data="hide"))
    return keyboard

