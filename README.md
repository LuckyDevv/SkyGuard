# 🔎 SkyGuard — Telegram-бот для проверки на скам

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://python.org)
[![Library](https://img.shields.io/badge/telebot-4.24-2CA5E0?style=flat-square&logo=telegram)](https://pypi.org/project/pyTelegramBotAPI/)

## 📌 О проекте

SkyGuard — бот безопасности для Telegram-сообществ: база скамеров и проверка
пользователей перед сделкой, каталог гарантов и стажёров, премиум-статусы,
статистика. Помогает сообществам бороться с мошенниками.

## ✨ Возможности

**Для пользователей:**
- `/check` (`чек`) — проверка пользователя по базе скамеров
- «слить скаммера» — добавление мошенника в базу с доказательствами
- «мой профиль» — репутация и статус пользователя
- «гаранты» — список проверенных гарантов (онлайн/офлайн)
- «стажёры» — список стажёров
- «частые вопросы» — FAQ
- «статистика» — статистика базы
- «премиум» — премиум-возможности

**Для администрации:**
- выдача/снятие премиума, управление гарантами и стажёрами
- управление базой скамеров

## 🧰 Стек

- Python 3.10+, pyTelegramBotAPI 4.24
- SQLite — база скамеров/профилей
- Работа с изображениями (доказательства)

## 🚀 Запуск

```bash
git clone https://github.com/LuckyDevv/SkyGuard.git
cd SkyGuard
pip install -r requirements.txt
# Токен бота задаётся в main.py (переменная TOKEN)
python main.py
```

## 📂 Структура

```
main.py                 # точка входа, меню и роутинг (RU-команды)
Utils/
  CommandHandler.py     # команды пользователей и админов
  QueryHandler.py       # callback-запросы
  DatabaseManager.py    # SQLite: скамеры, профили, статусы
  ConfigController.py   # JSON-конфиги
  Initializer.py        # инициализация окружения
images/                 # иллюстрации бота
```

## 📜 Лицензия

MIT
