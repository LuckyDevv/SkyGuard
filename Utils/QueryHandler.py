import os
from telebot.apihelper import ApiTelegramException
from Utils import Initializer
from Utils.DatabaseManager import DatabaseManager


class QueryHandler:
    def __init__(self, bot):
        self.bot = bot
        self.manager_db = DatabaseManager()
        self.img_dir = os.path.dirname(__file__)+"/../images/"

    def check_me(self, call):
        self.bot.answer_callback_query(call.id, "В разработке...")

    def theme(self, call):
        self.bot.answer_callback_query(call.id, "В разработке...")

    def country(self, call):
        self.bot.answer_callback_query(call.id, "В разработке...")

    def faq(self, call):
        self.bot.answer_callback_query(call.id)
        self.bot.delete_message(call.message.chat.id, call.message.message_id)
        self.bot.send_photo(
            call.message.chat.id,
            open(self.img_dir+"faq.jpg", "rb"),
            caption="<b>Я - SkyGuard</b> 💪🧬, бот, помогающий проверять людей на скам и сливать скаммеров.\n\n"
                    "/start\n"
                    "<i>- Перезапуск бота, если пропали кнопки</i> 🧬\n\n"
                    "/check (@юзер | ID проверяемого, без скобок)\n"
                    "<i>- Проверить человека на скам</i> 😳\n\n"
                    "/me\n"
                    "<i>- Ваш профиль</i> 👻\n\n"
                    "👇 <b>Остальной функционал доступен по кнопкам в меню</b>\n\n"
                    "Слить скаммера - @GasdReport",
            reply_markup=Initializer.get_faq2_keyboard(),
            parse_mode="HTML",
        )

    def faq_do(self, call):
        if call.data == "faq0":
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ Выберите вопрос из списка ниже:",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_keyboard()
            )
        elif call.data == "faq1":  # Кто такой гарант?
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ <b>Кто такой гарант?</b>\n\n"
                "Если коротко, то Гарант - это проверенный человек, выступающий посредником сделки, тем самым обеспечивая то, что никто из участников сделки не обманет.\n\n"
                "Обычно гарантов ищут по знакомствам. Спросите своих знакомых, кому можно доверить свои сделки.\n\n"
                "Не ведитесь на популярность. Очень часто медийки оказываются скаммерами, "
                "их популярность - конвейер доверчивых и не опытных людей. Не все такие, но суть в другом - "
                "оценивайте не по кол-ву подписчиков, а по репутации и узнаваемости человека.\n\n"
                "Также важны отзывы, но и они могут быть фейковыми. Обычно подделанные отзывы однотипные и выкладываются «пачками», "
                "то есть много отзывов за короткий отрезок времени",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_cancel_keyboard(),
                parse_mode="HTML"
            )
        elif call.data == "faq2":  # Как найти гаранта?
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ <b>Как найти гаранта?</b>\n\n"
                "В лс с ботом жмём кнопку «Гаранты» или вводим /mms.\n\n"
                "Бот отобразит вам проверенных людей, которые безопасно проведут сделку 😉\n\n"
                "<i>Если кнопок нет, пропишите /start</i>",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_cancel_keyboard(),
                parse_mode="HTML"
            )
        elif call.data == "faq3":  # Как стать стажёром?
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ <b>Как стать стажёром?</b>\n\n"
                "Следите за информацией в @GasdReport и участвуйте в наборах",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_cancel_keyboard(),
                parse_mode="HTML"
            )
        elif call.data == "faq4":  # Как стать гарантом?
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ <b>Как стать гарантом?</b>\n\n"
                "Мы не набираем гарантов. Готовы рассматривать лишь топов -> @BrandAPI",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_cancel_keyboard(),
                parse_mode="HTML"
            )
        elif call.data == "faq5":  # Как слить скаммера?
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ <b>Как слить скаммера?</b>\n\n"
                "Слить скаммера можно в нашей группе жалоб - @GasdReport\n"
                "- <i>Заходите в группу и кидаете пруфы скама, админы их рассматривают и принимают решение: заносить человека в базу или нет.</i>",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_cancel_keyboard(),
                parse_mode="HTML"
            )
        elif call.data == "faq6":  # Когда набор стажёров?
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ <b>Когда набор стажёров?</b>\n\n"
                "В среднем наборы проходят 2 раза в месяц",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_cancel_keyboard(),
                parse_mode="HTML"
            )
        elif call.data == "faq7":  # Можно ли купить роль в базе?
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ <b>Можно ли купить роль в базе?</b>\n\n"
                "НЕТ. Мы НЕ продаём админки/ роли гарантов в нашей базе. Если вы хотите поддержать нашу базу - /premium",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_cancel_keyboard(),
                parse_mode="HTML"
            )
        elif call.data == "faq8":  # Можно ли купить снятие из базы?
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                "💁‍♂️ <b>Можно ли купить снятие из базы?</b>\n\n"
                "НЕТ. Мы НЕ удаляем пользователей. Наша цель - быть надёжным и честным источником информации, который сможет помочь людям.",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_faq_cancel_keyboard(),
                parse_mode="HTML"
            )
        else:
            self.bot.answer_callback_query(call.id, "Ошибка в запросе.")

    def hide_message(self, call):
        try:
            self.bot.delete_message(call.message.chat.id, call.message.message_id)
        except ApiTelegramException:
            pass
        self.bot.answer_callback_query(call.id)

    def stats(self, call):
        if call.data == "stats0":
            self.bot.answer_callback_query(call.id)
            self.bot.edit_message_caption(
                f"<a href='https://t.me/{call.from_user.username}'>{call.from_user.first_name}</a>, ниже находится статистика SkyGuard:\n\n"
                        f"🚫 Скаммеров в базе: {self.manager_db.scammers_count()}\n"
                        f"👁️ Пользователей бота: {self.manager_db.users_count()}\n\n"
                        f"⚖️ Админов: {self.manager_db.admins_count()}\n"
                        f"💸 Гарантов: {self.manager_db.brokers_count()}\n"
                        f"🏆️ Проверенных: {self.manager_db.trust_count()}\n\n"
                        f"🎉 Бот уже в {self.manager_db.groups_count()} группах\n\n"
                        f"🔎 Поисков по базе за всё время: {self.manager_db.finds_count()}\n"
                        f"🌴 В последний раз искали: {self.manager_db.last_find()}",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_stats_keyboard(),
                parse_mode="HTML"
            )
        elif call.data == "stats1":
            self.bot.answer_callback_query(call.id)
            top_merged = self.manager_db.top_merged()
            if top_merged is not None:
                text = f"🏆 <b>Топ по количеству слитых скаммеров:</b>\n\n{top_merged}"
            else:
                text = "🏆 <b>Топ по количеству слитых скаммеров пока что пуст :(</b>"
            self.bot.edit_message_caption(
                text,
                call.message.chat.id,
                call.message.message_id,
                parse_mode="HTML",
                reply_markup=Initializer.get_stats1_keyboard()
            )
        elif call.data == "stats2":
            self.bot.answer_callback_query(call.id)
            top_popular = self.manager_db.top_popular()
            if top_popular is not None:
                text = f"🏆 <b>Топ самых популярных пользователей:</b>\n\n{top_popular}"
            else:
                text = "🏆 <b>Топ самых популярных пользователей что пуст :(</b>"
            self.bot.edit_message_caption(
                text,
                call.message.chat.id,
                call.message.message_id,
                parse_mode="HTML",
                reply_markup=Initializer.get_stats2_keyboard()
            )


    def premium(self, call):
        if call.data == "premium0":
            self.bot.edit_message_caption(
                "<b>Откройте уникальные возможности:</b>\n\n"
                "• Ставить анимированные темы\n"
                "• Установить себе кастомное фото\n"
                "• Поставить ссылку на свой канал\n"
                "• Получать уведомления о том, что вас искали\n"
                "• Проверять больше людей (х2 проверок в день)\n\n"
                "<b>Все эти фишки входят в SkyGuard Premium</b>",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_premium_keyboard(),
                parse_mode="HTML"
            )
            return
        if call.from_user.username == "" or call.from_user.username is None:
            user = f"#id{call.from_user.id}"
        else:
            user = "@"+call.from_user.username
        if call.data == "premium12m":
            product_name = "«Премиум | 12 месяцев»"
            product_price = 999
        elif call.data == "premium3m":
            product_name = "«Премиум | 3 месяца»"
            product_price = 499
        elif call.data == "premium1m":
            product_name = "«Премиум | 1 месяц»"
            product_price = 199
        else:
            self.bot.edit_message_caption(
                "Вы выбрали неизвестный товар!",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=Initializer.get_premium_cancel_keyboard(),
            )
            return
        self.bot.edit_message_caption(
            f"Для покупки товара {product_name} за {product_price} ₽ - напишите @sky4arg следующий текст:\n\n"
            f"<pre>Я, {user}, хочу купить товар {product_name} за {product_price} ₽ в боте @sasd_test_bot</pre>\n\n"
            f"Просьба не спамить! Отправили данное сообщение - ждите ответа, не нужно писать сотни сообщений.",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=Initializer.get_premium_cancel_keyboard(),
            parse_mode="HTML"
        )

    def profile(self, call):
        self.bot.answer_callback_query(call.id)
        user_id = call.from_user.id
        username = call.from_user.username
        role = self.manager_db.role_get(user_id, username)
        if role is None or role == "user":
            image = open(self.img_dir + "empty.jpg", "rb")
        else:
            try:
                image = open(self.img_dir + f"{role}.jpg", "rb")
            except FileNotFoundError:
                image = open(self.img_dir + "empty.jpg", "rb")
        self.bot.delete_message(call.message.chat.id, call.message.message_id)
        self.bot.send_photo(
            call.message.chat.id,
            image,
            caption=f"ℹ️ <a href='https://t.me/{username}'>{call.from_user.first_name}</a>, Ваш профиль:\n\n"
                    f"🔥 Скаммеров слито: {self.manager_db.merged_get(username, user_id)}\n"
                    f"🔎 Вас искали {self.manager_db.finds_get(username, user_id)} раз\n\n"
                    f"👑 SkyGuard Premium " + ("✅" if self.manager_db.premium_check(username, user_id) else "❌") + "\n"
                                                                                                                  f"🏖 Сегодня вам доступно ещё {self.manager_db.checks_get(username, user_id)} проверки",
            reply_markup=Initializer.get_profile_keyboard(),
            parse_mode="HTML"
        )
