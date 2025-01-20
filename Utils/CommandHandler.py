import os

from Utils import Initializer
from Utils.DatabaseManager import DatabaseManager


class CommandHandler:
    def __init__(self, bot):
        self.bot = bot
        self.manager_db = DatabaseManager()
        self.img_dir = os.path.dirname(__file__)+"/../images/"

    def my_profile_cmd(self, message):
        user_id = message.from_user.id
        username = message.from_user.username
        role = self.manager_db.role_get(user_id, username)

        if role is None or role == "user":
            image = open(self.img_dir+"empty.jpg", "rb")
        else:
            try:
                image = open(self.img_dir + f"{role}.jpg", "rb")
            except FileNotFoundError:
                image = open(self.img_dir + "empty.jpg", "rb")
        self.bot.send_photo(
            message.chat.id,
            image,
            caption=f"ℹ️ <a href='https://t.me/{username}'>{message.from_user.first_name}</a>, Ваш профиль:\n\n"
                    f"🔥 Скаммеров слито: {self.manager_db.merged_get(username, user_id)}\n"
                    f"🔎 Вас искали {self.manager_db.finds_get(username, user_id)} раз\n\n"
                    f"👑 SkyGuard Premium "+("✅" if self.manager_db.premium_check(username, user_id) else "❌")+"\n"
                    f"🏖 Сегодня вам доступно ещё {self.manager_db.checks_get(username, user_id)} проверки",
            reply_markup=Initializer.get_profile_keyboard(),
            parse_mode="HTML"
        )

    def merge_cmd(self, message):
        self.bot.send_photo(
            message.chat.id,
            open(self.img_dir+"merge.jpg", "rb"),
            caption="<b>😮‍💨 Если вы стали жертвой мошенников - жмите кнопку «Написать жалобу»</b>\n\n"
                    "👩‍💻 Вы будете направлены в чат с нашими волонтёрами, они разберутся в ситуации и занесут мошенника в базу. Это бесплатно",
            reply_markup=Initializer.get_merge_keyboard(),
            parse_mode="HTML"
        )

    def faq_cmd(self, message):
        self.bot.send_photo(
            message.chat.id,
            open(self.img_dir+"faq.jpg", "rb"),
            caption="💁‍♂️ Выберите вопрос из списка ниже:",
            reply_markup=Initializer.get_faq_keyboard(),
        )

    def brokers_cmd(self, message):
        list_users = self.manager_db.brokers_get()
        if list_users is None:
            text = "️‍❤️‍🔥 Сейчас в SkyGuard нет активных гарантов"
        else:
            text = "❤️‍🔥 Ниже приведён список гарантов SkyGuard (первые 20), которым можно доверять:"
        self.bot.send_photo(
            message.chat.id,
            open(self.img_dir+"brokers.jpg", "rb"),
            caption=text,
            reply_markup=Initializer.get_list_keyboard(self.manager_db.brokers_get()),
        )

    def interns_command(self, message):
        list_users = self.manager_db.interns_get()
        if list_users is None:
            text = "🌴 Сейчас в SkyGuard нет активных стажёров"
        else:
            text = "🌴 Ниже приведён список стажёров (первые 20) SkyGuard:"
        self.bot.send_photo(
            message.chat.id,
            open(self.img_dir+"brokers.jpg", "rb"),
            caption=text,
            reply_markup=Initializer.get_list_keyboard(list_users),
        )

    def stats_cmd(self, message):
        self.bot.send_photo(
            message.chat.id,
            open(self.img_dir+"stats.jpg", "rb"),
            caption=f"<a href='https://t.me/{message.from_user.username}'>{message.from_user.first_name}</a>, ниже находится статистика SkyGuard:\n\n"
                    f"🚫 Скаммеров в базе: {self.manager_db.scammers_count()}\n"
                    f"👁️ Пользователей бота: {self.manager_db.users_count()}\n\n"
                    f"⚖️ Админов: {self.manager_db.admins_count()}\n"
                    f"💸 Гарантов: {self.manager_db.brokers_count()}\n"
                    f"🏆️ Проверенных: {self.manager_db.trust_count()}\n\n"
                    f"🎉 Бот уже в {self.manager_db.groups_count()} группах\n\n"
                    f"🔎 Поисков по базе за всё время: {self.manager_db.finds_count()}\n"
                    f"🌴 В последний раз искали: {self.manager_db.last_find()}",
            reply_markup=Initializer.get_stats_keyboard(),
            parse_mode="HTML"
        )

    def premium_cmd(self, message):
        self.bot.send_photo(
            message.chat.id,
            open(self.img_dir+"premium.jpg", "rb"),
            caption="<b>Откройте уникальные возможности:</b>\n\n"
                    "• Ставить анимированные темы\n"
                    "• Установить себе кастомное фото\n"
                    "• Поставить ссылку на свой канал\n"
                    "• Получать уведомления о том, что вас искали\n"
                    "• Проверять больше людей (х2 проверок в день)\n\n"
                    "<b>Все эти фишки входят в SkyGuard Premium</b>",
            reply_markup=Initializer.get_premium_keyboard(),
            parse_mode="HTML"
        )

    def check_cmd(self, message):
        user_id = message.from_user.id

    def scam_cmd(self, message):
        user_id = message.from_user.id

    def give_premium_cmd(self, message):
        user_id = message.from_user.id

    def add_broker_cmd(self, message):
        user_id = message.from_user.id

    def remove_broker_cmd(self, message):
        user_id = message.from_user.id

    def add_intern_cmd(self, message):
        user_id = message.from_user.id

    def remove_intern_cmd(self, message):
        user_id = message.from_user.id

    def thanks_cmd(self, message):
        user_id = message.from_user.id

    def add_warn_cmd(self, message):
        user_id = message.from_user.id

    def remove_warn_cmd(self, message):
        user_id = message.from_user.id

    def mail_cmd(self, message):
        user_id = message.from_user.id

    def add_trust_cmd(self, message):
        user_id = message.from_user.id

    def remove_trust_cmd(self, message):
        user_id = message.from_user.id

    def mute_cmd(self, message):
        user_id = message.from_user.id

    def unmute_cmd(self, message):
        user_id = message.from_user.id

    def ban_cmd(self, message):
        user_id = message.from_user.id

    def unban_cmd(self, message):
        user_id = message.from_user.id

    def kick_cmd(self, message):
        user_id = message.from_user.id

    def todo(self):
        pass

