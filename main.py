import os
import telebot

from Utils.CommandHandler import CommandHandler
from Utils.DatabaseManager import DatabaseManager

# Тестовый бот 7829240892:AAGTdtDQ_Jw5eJuQ9MKo8uQNDEeyJJgn3xQ
# Продакшн бот
TOKEN = "7829240892:AAGTdtDQ_Jw5eJuQ9MKo8uQNDEeyJJgn3xQ"  # Введите сюда токен своего Telegram-бота
bot = telebot.TeleBot(TOKEN)
bot.set_webhook()
images_directory = os.path.dirname(__file__)+"/images/"
database_manager = DatabaseManager()
command_handler = CommandHandler(bot, database_manager)

menu_commands = {
    "мой профиль": command_handler.my_profile_cmd,
    "слить скаммера": command_handler.merge_cmd,
    "частые вопросы": command_handler.faq_cmd,
    "гаранты": command_handler.brokers_cmd,
    "волонтёры": command_handler.volunteers_cmd,
    "статистика": command_handler.stats_cmd,
    "премиум": command_handler.premium_cmd
}

commands = {
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
    # Список волонтёров
    "/волонтёры": command_handler.volunteers_cmd,
    "/волонтеры": command_handler.volunteers_cmd,
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
    # Добавить волонтёра
    "+волонтер": command_handler.add_volunteer_cmd,
    "+волонтёр": command_handler.add_volunteer_cmd,
    # Убрать волонтёра
    "-волонтер": command_handler.remove_volunteer_cmd,
    "-волонтёр": command_handler.remove_volunteer_cmd,
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

}


@bot.message_handler(content_types=["text"])
def t1(message):
    command = message.text.split()[0]
    if command == '/help':
        return
    if message.chat.type == "private":
        pass
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        pass



@bot.callback_query_handler(func=lambda call: call.data)
def q1(call):
    pass


bot.infinity_polling(timeout=10, long_polling_timeout=5)
