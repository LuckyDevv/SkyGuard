import os
import sqlite3
import sys
from sqlite3 import IntegrityError
from time import strftime, gmtime
from telebot.apihelper import ApiTelegramException
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from Utils.ConfigController import ConfigController, ConfigType


class DatabaseManager:
    def __init__(self):
        directory = os.path.dirname(__file__)
        self.db = sqlite3.connect(
            directory+"/../Users_DB.sqlite3",
            check_same_thread=False,
        )
        self.cur = self.db.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS `users` ("
            "`user_id` INTEGER PRIMARY KEY,"
            " `username` TEXT,"
            " `first_name` TEXT,"
            " `finds` INTEGER,"
            " `merged` INTEGER,"
            " `role` INTEGER,"
            " `warns` INTEGER,"
            " `is_premium` BOOLEAN,"
            " `end_premium` TIMESTAMP,"
            " `country` TEXT,"
            " `checks` INTEGER,"
            " `channel` TEXT"
            ");"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS `reputations` ("
            "`user_id` INTEGER,"
            "`username` TEXT,"
            " `reputation` INTEGER,"
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