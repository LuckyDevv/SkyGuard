import os
import telebot
from Utils import Initializer
from Utils.CommandHandler import CommandHandler
from Utils.DatabaseManager import DatabaseManager
from Utils.QueryHandler import QueryHandler

TOKEN = ""  # Введите сюда токен своего Telegram-бота
bot = telebot.TeleBot(TOKEN)
bot.set_webhook()
images_directory = os.path.dirname(__file__)+"/images/"
database_manager = DatabaseManager()
command_handler = CommandHandler(bot)
query_handler = QueryHandler(bot)
user_image = []
user_channel = []

menu_commands = {
    "мой профиль": command_handler.my_profile_cmd,
    "слить скаммера": command_handler.merge_cmd,
    "частые вопросы": command_handler.faq_cmd,
    "гаранты": command_handler.brokers_cmd,
    "стажёры": command_handler.interns_command,
    "стажеры": command_handler.interns_command,
    "статистика": command_handler.stats_cmd,
    "премиум": command_handler.premium_cmd
}
commands = {
    # Просмотреть свой профиль
    "/profile": command_handler.my_profile_cmd,
    "/профиль": command_handler.my_profile_cmd,
    "profile": command_handler.my_profile_cmd,
    "профиль": command_handler.my_profile_cmd,
    # Чекнуть юзера в базе
    "/check": command_handler.check_cmd,
    "check": command_handler.check_cmd,
    "чек": command_handler.check_cmd,
    "/чек": command_handler.check_cmd,
    # Посмотреть свой профиль
    "/me": command_handler.my_profile_cmd,
    "me": command_handler.my_profile_cmd,
    "ми": command_handler.my_profile_cmd,
    "/ми": command_handler.my_profile_cmd,
    # Просмотреть премиум
    "/премиум": command_handler.premium_cmd,
    "/premium": command_handler.premium_cmd,
    # Просмотреть статистику бота
    "/stats": command_handler.stats_cmd,
    "/стата": command_handler.stats_cmd,
    "стата": command_handler.stats_cmd,
    # Внести чела в базу скаммеров
    "/scam": command_handler.scam_cmd,
    "scam": command_handler.scam_cmd,
    # Выдать премиум
    "/прем": command_handler.give_premium_cmd,
    "/prem": command_handler.give_premium_cmd,
    # Список гарантов
    "/mms": command_handler.brokers_cmd,
    "/гаранты": command_handler.brokers_cmd,
    # Список стажёров
    "/стажёры": command_handler.interns_command,
    "/стажеры": command_handler.interns_command,
    # Слить скаммера в чат
    "/слить": command_handler.merge_cmd,
    "/merge": command_handler.merge_cmd,
    # Вопросы и ответы
    "/чта": command_handler.faq_cmd,
    "/вио": command_handler.faq_cmd,
    "/faq": command_handler.faq_cmd,
    "/qna": command_handler.faq_cmd,
    # Добавить гаранта
    "+гарант": command_handler.add_broker_cmd,
    # Снять гаранта
    "-гарант": command_handler.remove_broker_cmd,
    # Добавить стажёра
    "+стажёр": command_handler.add_intern_cmd,
    "+стажер": command_handler.add_intern_cmd,
    # Убрать стажёра
    "-стажёр": command_handler.remove_intern_cmd,
    "-стажер": command_handler.remove_intern_cmd,
    # Выдать юзеру +1 слитый скаммер
    "+спс": command_handler.thanks_cmd,
    "+спасибо": command_handler.thanks_cmd,
    "+thanks": command_handler.thanks_cmd,
    "+thx": command_handler.thanks_cmd,
    # Выдать выговор
    "+выговор": command_handler.add_warn_cmd,
    "+выг": command_handler.add_warn_cmd,
    "+warn": command_handler.add_warn_cmd,
    "+варн": command_handler.add_warn_cmd,
    # Снять выговор
    "-выговор": command_handler.remove_warn_cmd,
    "-выг": command_handler.remove_warn_cmd,
    "-warn": command_handler.remove_warn_cmd,
    "-варн": command_handler.remove_warn_cmd,
    # Создать рассылку
    "+рассылка": command_handler.mail_cmd,
    "/рассылка": command_handler.mail_cmd,
    "/mail": command_handler.mail_cmd,
    "/mailing": command_handler.mail_cmd,
    "+mail": command_handler.mail_cmd,
    "+mailing": command_handler.mail_cmd,
    # Выдать траст
    "+траст": command_handler.add_trust_cmd,
    "+trust": command_handler.add_trust_cmd,
    # Забрать траст
    "-траст": command_handler.remove_trust_cmd,
    "-trust": command_handler.remove_trust_cmd
}
chat_commands = {
    # Выдать мут
    "/mute": command_handler.mute_cmd,
    "/мут": command_handler.mute_cmd,
    "/делмут": command_handler.mute_cmd,
    "/delmute": command_handler.mute_cmd,
    # Снять мут
    "/рмут": command_handler.unmute_cmd,
    "/анмут": command_handler.unmute_cmd,
    "/unmute": command_handler.unmute_cmd,
    # Заблокировать в группе
    "/бан": command_handler.ban_cmd,
    "/ban": command_handler.ban_cmd,
    # Разблокировать в группе
    "/рбан": command_handler.unban_cmd,
    "/анбан": command_handler.unban_cmd,
    "/унбан": command_handler.unban_cmd,
    "/разбан": command_handler.unban_cmd,
    "/пардон": command_handler.unban_cmd,
    "/pardon": command_handler.unban_cmd,
    "/unban": command_handler.unban_cmd,
    # Кикнуть из группы
    "/kick": command_handler.kick_cmd,
    "/выгнать": command_handler.kick_cmd,
    "/кик": command_handler.kick_cmd
}
queries = {
    "profile": query_handler.profile,  # Вернуться в профиль
    "checkme": query_handler.check_me,  # Проверить себя
    "theme": query_handler.theme,  # Сменить тему проверки
    "country": query_handler.country,  # Сменить страну
    "faq": query_handler.faq,  # "Как пользоваться ботом?"
    "hide": query_handler.hide_message,  # Кнопка "Скрыть"
    "faq0": query_handler.faq_do,  # Возрат к списку частых вопросов
    "faq1": query_handler.faq_do,  # "Кто такой гарант?"
    "faq2": query_handler.faq_do,  # "Как найти гаранта?"
    "faq3": query_handler.faq_do,  # "Как стать стажёром?"
    "faq4": query_handler.faq_do,  # "Как стать гарантом?"
    "faq5": query_handler.faq_do,  # "Как слить скаммера?"
    "faq6": query_handler.faq_do,  # "Когда набор стажёров?"
    "faq7": query_handler.faq_do,  # "Можно ли купить роль в базе?"
    "faq8": query_handler.faq_do,  # "Можно ли купить снятие из базы?"
    "stats0": query_handler.stats,  # Статистика бота
    "stats1": query_handler.stats,  # Топ по сливам
    "stats2": query_handler.stats,  # Топ популярных
    "premium12m": query_handler.premium,  # Премиум на 12 мес
    "premium3m": query_handler.premium,  # Премиум на 3 мес
    "premium1m": query_handler.premium,  # Премиум на 1 мес
    "premium0": query_handler.premium,  # Вернуться к меню премиума
}


@bot.message_handler(content_types=["photo"])
def p1(message):
    if message.chat.type == "private":
        user_id = int(message.from_user.id)
        if user_id in user_image:
            file_id = max(message.photo, key=lambda x: x.height).file_id
            if database_manager.picture_set(user_id, message.from_user.username, file_id):
                bot.send_photo(
                    message.chat.id,
                    file_id,
                    "❤️ Вы успешно изменили картинку своего профиля!"
                )
            else:
                bot.reply_to(
                    message,
                    "❌ Не удалось изменить картинку профиля! :("
                )
            user_image.remove(user_id)


@bot.message_handler(content_types=["text"])
def t1(message):
    command = message.text.split()[0]
    if message.chat.type == "private":
        user_id = int(message.from_user.id)
        if user_id in user_channel:
            if len(message.text) < 75:
                if database_manager.channel_set(user_id, message.from_user.username, message.text):
                    bot.send_message(
                        message.chat.id,
                        f"✅ Вы успешно изменили свой канал на: «{message.text}!»"
                    )
                else:
                    bot.send_message(
                        message.chat.id,
                        "❌ Не удалось изменить ваш канал! :("
                    )
            else:
                bot.send_message(
                    message.chat.id,
                    "❌ Текст слишком большой! Максимальная длина - 75 символов."
                )
            user_channel.remove(user_id)
            return
        if not database_manager.user_exists(message.from_user.id, message.from_user.username):
            if not database_manager.user_create(message.from_user.username, message.from_user.id, message.from_user.first_name):
                bot.send_message(
                    message.chat.id,
                    "Не удалось зарегистрировать вас! Попробуйте позже."
                )
                bot.send_message(
                    1199296238,
                    f"Не удалось зарегистрировать пользователя!\n\n"
                    f"ID: {message.from_user.id}\n"
                    f"Username: {message.from_user.username}\n"
                    f"Frist_Name: {message.from_user.first_name}"
                )
        if command == '/start':
            bot.send_photo(
                message.chat.id,
                open(images_directory + "hello.jpg", "rb"),
                "<b>Мы - <a href='https://t.me/sasd_test_bot'>SkyGuard</a>, глобальная АнтиСкам база нового поколения:</b>\n\n"
                "🤓 Проверим человека на скам\n"
                "🤠 Найдём проверенного гаранта\n"
                "🤕 Поможем слить скаммера\n\n"
                "ℹ️ Попробуйте пробить человека - напишите\n"
                "<pre>чек @sky4arg</pre>",
                parse_mode="HTML",
                reply_markup=Initializer.get_start_keyboard()
            )
        else:
            if command in commands:
                commands[command](message)
            else:
                for menu_command in menu_commands:
                    if message.text.lower().__contains__(menu_command):
                        menu_commands[menu_command](message)
                        return
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        pass


@bot.callback_query_handler(func=lambda call: call.data)
def q1(call):
    user_id = call.from_user.id
    if call.data == "custom-image":
        if database_manager.premium_check(user_id, call.from_user.username):
            if user_id in user_channel:
                bot.answer_callback_query(call.id, "❌ Сначала завершите или отмените прошлое действие!")
                return
            if user_id not in user_image:
                user_image.append(user_id)
            bot.answer_callback_query(call.id)
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption="🖼 Отлично! Теперь отправьте картинку, которую хотите установить в свой профиль!",
                reply_markup=Initializer.get_custom_image_keyboard()
            )
        else:
            bot.answer_callback_query(call.id, "❌ Чтобы поставить свою картинку, нужен SkyGuard Premium (/premium)", True)
    elif call.data == "channel":
        if database_manager.premium_check(user_id, call.from_user.username):
            if user_id in user_image:
                bot.answer_callback_query(call.id, "❌ Сначала завершите или отмените прошлое действие!")
                return
            if user_id not in user_channel:
                user_channel.append(user_id)
            bot.answer_callback_query(call.id)
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption="📝 Отлично! Теперь отправьте текст, которую хотите установить в свой профиль!",
                reply_markup=Initializer.get_channel_keyboard()
            )
        else:
            bot.answer_callback_query(call.id, "❌ Чтобы поставить свою картинку, нужен SkyGuard Premium (/premium)", True)
    elif call.data == "custom-image-cancel":
        bot.answer_callback_query(call.id)
        if user_id in user_image:
            user_image.remove(user_id)
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption="🙅‍♂️ Вы успешно отменили смену картинки профиля!",
                reply_markup=Initializer.get_profile_keyboard()
            )
    elif call.data == "channel-cancel":
        bot.answer_callback_query(call.id)
        if user_id in user_channel:
            user_channel.remove(user_id)
            bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption="🙅‍♂️ Вы успешно отменили смену канала профиля!",
                reply_markup=Initializer.get_profile_keyboard()
            )
    elif call.data in queries:
        queries[call.data](call)


bot.infinity_polling(timeout=10, long_polling_timeout=5)
