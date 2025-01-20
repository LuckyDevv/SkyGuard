import os
import sqlite3
from sqlite3 import OperationalError, ProgrammingError

from Utils.ConfigController import ConfigController, ConfigType


class DatabaseManager:
    def __init__(self):
        directory = os.path.dirname(__file__)
        self.db = sqlite3.connect(
            directory+"/../SkyGuard_DB.sqlite3",
            check_same_thread=False,
        )
        self.cur = self.db.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS `users` ("
            "`user_id` INTEGER PRIMARY KEY,"
            "`username` TEXT,"
            "`first_name` TEXT,"
            "`finds` INTEGER,"
            "`merged` INTEGER,"
            "`role` TEXT,"
            "`warns` INTEGER,"
            "`is_premium` BOOLEAN,"
            "`end_premium` TIMESTAMP,"
            "`country` TEXT,"
            "`checks` INTEGER,"
            "`channel` TEXT,"
            "`custom_image` TEXT,"
            "`theme` INTEGER"
            ");"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS `reputations` ("
            "`user_id` INTEGER,"
            "`username` TEXT,"
            "`reputation` INTEGER,"
            "PRIMARY KEY(`user_id`, `username`)"
            ");"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS `scammers` ("
            "`user_id` INTEGER,"
            "`username` TEXT,"
            "`description` TEXT,"
            "`role` TEXT,"
            "PRIMARY KEY(`user_id`, `username`)"
            ");"
        )
        self.stats_config = ConfigController(directory+"/../stats_config.json", ConfigType.JSON)
        if not self.stats_config.exists("total_finds"):
            self.stats_config.set("total_finds", 0)
            self.stats_config.set("total_groups", 0)
            self.stats_config.set("last_find", "")
            self.stats_config.save()
        self.db.commit()

    def user_exists(self, user_tc1, user_tc2):
        try:
            fetch = self.cur.execute("SELECT 1 FROM `users` WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?", (user_tc1, user_tc2, user_tc2, user_tc1)).fetchone()
            if fetch is not None and fetch[0] == 1:
                return True
            else:
                return False
        except (OperationalError, ProgrammingError) as e:
            print(e)
            return False

    def user_create(self, username, user_id, first_name):
        try:
            self.cur.execute(
                "INSERT INTO `users` (`user_id`, `username`, `first_name`, `finds`, `merged`, `role`, `warns`, `is_premium`, `end_premium`, `country`, `checks`, `channel`, `custom_image`, `theme`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (user_id, username, first_name, 0, 0, 'user', 0, 0, None, None, 25, None, None, 'default'))
            self.db.commit()
            return True
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return False

    def merged_get(self, user_tc1, user_tc2):
        try:
            fetch = self.cur.execute("SELECT `merged` FROM `users` WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?", (user_tc1, user_tc2, user_tc2, user_tc1)).fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return None
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return None

    def merged_add(self, user_tc1, user_tc2):
        merged = self.merged_get(user_tc1, user_tc2)
        if merged is not None and type(merged) is int:
            merged += 1
            try:
                self.cur.execute(
                    "UPDATE `users` SET `merged`=? WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                    (merged, user_tc1, user_tc2, user_tc2, user_tc1))
                self.db.commit()
                return True
            except OperationalError as e:
                print(e)
                return False
        return False

    def finds_get(self, user_tc1, user_tc2):
        try:
            fetch = self.cur.execute(
                "SELECT `finds` FROM `users` WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                (user_tc1, user_tc2, user_tc2, user_tc1)).fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return None
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return None

    def finds_add(self, user_tc1, user_tc2):
        finds = self.finds_get(user_tc1, user_tc2)
        if finds is not None and type(finds) is int:
            finds += 1
            try:
                self.cur.execute(
                    "UPDATE `users` SET `finds`=? WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                    (finds, user_tc1, user_tc2, user_tc2, user_tc1))
                self.db.commit()
                return True
            except OperationalError as e:
                print(e)
                return False
        return False

    def checks_get(self, user_tc1, user_tc2):
        try:
            fetch = self.cur.execute(
                "SELECT `checks` FROM `users` WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                (user_tc1, user_tc2, user_tc2, user_tc1)).fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return None
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return None

    def checks_reduce(self, user_tc1, user_tc2):
        checks = self.finds_get(user_tc1, user_tc2)
        if checks is not None and type(checks) is int:
            checks -= 1
            try:
                self.cur.execute(
                    "UPDATE `users` SET `checks`=? WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                    (checks, user_tc1, user_tc2, user_tc2, user_tc1))
                self.db.commit()
                return True
            except OperationalError as e:
                print(e)
                return False
        return False

    def checks_reset(self):
        try:
            self.cur.execute("UPDATE users SET checks = CASE WHEN is_premium = 1 THEN 50 ELSE 25 END;")
            self.db.commit()
            return True
        except OperationalError as e:
            print(e)
            return False

    def premium_check(self, user_tc1, user_tc2):
        try:
            fetch = self.cur.execute(
                "SELECT `is_premium` FROM `users` WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                (user_tc1, user_tc2, user_tc2, user_tc1)).fetchone()
            if fetch is not None:
                if fetch[0] == 1:
                    return True
            return False
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return False

    def role_get(self, user_tc1, user_tc2):
        try:
            fetch = self.cur.execute(
                "SELECT `role` FROM `users` WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                (user_tc1, user_tc2, user_tc2, user_tc1)).fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return None
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return None

    def scammers_count(self):
        try:
            fetch = self.cur.execute(
                "SELECT COUNT(*) AS user_count FROM users WHERE role IN ('scammer', 'cock', 'maybe')").fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return 0
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return 0

    def users_count(self):
        try:
            fetch = self.cur.execute(
                "SELECT COUNT(*) AS user_count FROM users").fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return 0
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return 0

    def admins_count(self):
        try:
            fetch = self.cur.execute(
                "SELECT COUNT(*) AS user_count FROM users WHERE role IN ('intern', 'admin', 'director', 'owner', 'president')").fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return 0
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return 0

    def brokers_count(self):
        try:
            fetch = self.cur.execute(
                "SELECT COUNT(*) AS user_count FROM users WHERE role='broker'").fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return 0
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return 0

    def trust_count(self):
        try:
            fetch = self.cur.execute(
                "SELECT COUNT(*) AS user_count FROM users WHERE role='trust'").fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return 0
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return 0

    def groups_count(self):
        return self.stats_config.get("total_groups", 0)

    def finds_count(self):
        return self.stats_config.get("total_finds", 0)

    def last_find(self):
        last = self.stats_config.get("last_find", "")
        if last == "":
            return "Неизвестно"
        return last

    def picture_get(self, user_tc1, user_tc2):
        try:
            fetch = self.cur.execute(
                "SELECT `custom_image` FROM `users` WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                (user_tc1, user_tc2, user_tc2, user_tc1)).fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return None
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return None

    def picture_set(self, user_tc1, user_tc2, picture):
        try:
            self.cur.execute("UPDATE `users` SET `custom_image`=? WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=? AND `is_premium`=1", (picture, user_tc1, user_tc2, user_tc2, user_tc1))
            self.db.commit()
            return True
        except OperationalError as e:
            print(e)
            return False

    def channel_get(self, user_tc1, user_tc2):
        try:
            fetch = self.cur.execute(
                "SELECT `channel` FROM `users` WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=?",
                (user_tc1, user_tc2, user_tc2, user_tc1)).fetchone()
            if fetch is not None:
                return fetch[0]
            else:
                return None
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return None

    def channel_set(self, user_tc1, user_tc2, channel):
        try:
            self.cur.execute("UPDATE `users` SET `channel`=? WHERE `username`=? OR `user_id`=? OR `username`=? OR `user_id`=? AND `is_premium`=1", (channel, user_tc1, user_tc2, user_tc2, user_tc1))
            self.db.commit()
            return True
        except (OperationalError,ProgrammingError) as e:
            print(e)
            return False

    def top_merged(self):
        try:
            fetch = self.cur.execute("SELECT `username`,`first_name`,`merged` FROM users ORDER BY merged DESC LIMIT 5;").fetchall()
            if fetch is not None:
                if len(fetch) > 0:
                    nums = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
                    result = ""
                    count = 0
                    for user in fetch:
                        if user[0] == "":
                            link = user[1]
                        else:
                            link = f"<a href='https://t.me/{user[0]}'>{user[1]}</a>\n"
                        result += nums[count]+f" 🥷 {user[2]} {link}"
                        count += 1
                    if result != "":
                        return result
        except (OperationalError,ProgrammingError) as e:
            print(e)
        return None

    def top_popular(self):
        try:
            fetch = self.cur.execute("SELECT `username`,`first_name`,`finds` FROM users ORDER BY finds DESC LIMIT 5;").fetchall()
            if fetch is not None:
                if len(fetch) > 0:
                    nums = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
                    result = ""
                    count = 0
                    for user in fetch:
                        if user[0] == "":
                            link = user[1]
                        else:
                            link = f"<a href='https://t.me/{user[0]}'>{user[1]}</a>\n"
                        result += nums[count] + f" 😸 {user[2]} {link}"
                        count += 1
                    if result != "":
                        return result
        except (OperationalError,ProgrammingError) as e:
            print(e)
        return None

    def brokers_get(self):
        try:
            fetch = self.cur.execute("SELECT `username`,`first_name` FROM `users` WHERE `role`='broker' ORDER BY merged DESC LIMIT 20").fetchall()
            if fetch is not None:
                if len(fetch) > 0:
                    return fetch
        except (OperationalError,ProgrammingError) as e:
            print(e)
        return None

    def interns_get(self):
        try:
            fetch = self.cur.execute("SELECT `username`,`first_name` FROM `users` WHERE `role`='intern' ORDER BY merged DESC LIMIT 20").fetchall()
            if fetch is not None:
                if len(fetch) > 0:
                    return fetch
        except (OperationalError, ProgrammingError) as e:
            print(e)
        return None
