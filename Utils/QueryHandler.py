class QueryHandler:
    def __init__(self, bot, manager_db, user_kb, grant_kb, admin_kb, ab_kb):
        self.bot = bot
        self.manager_db = manager_db
        self.keyboards = [user_kb, grant_kb, admin_kb, ab_kb]

