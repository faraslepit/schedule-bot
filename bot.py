import os
import datetime
import telebot
import threading
import http.server
import socketserver
from telebot import types
import random

PORT = int(os.environ.get("PORT", 8000))

class HealthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

def run_health_server():
    with socketserver.TCPServer(("", PORT), HealthHandler) as httpd:
        print(f"Health server running on port {PORT}")
        httpd.serve_forever()

threading.Thread(target=run_health_server, daemon=True).start()

START_DATE = datetime.date(2026, 1, 12)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

SCHEDULE_1 = {
    "Числитель": {
        "Понедельник": [
            "8:30-10:00 Физика (пр 425-3)",
            "10:20-11:50 Математика (пр 121-3)",
            "12:10-13:40 Математика (лк А-3)",
            "14:00-15:30 История (лк А-3)"
        ],
        "Вторник": [
            "8:30-10:00 Английский (пр 303а-1)",
            "10:20-11:50 Математика (лк 433-3)",
            "12:10-13:40 Физкультура",
            "14:00-15:30 ОИБ (лк 408-2)"
        ],
        "Среда": [
            "10:20-11:50 ТОИ (Матвеева, лабы 428-2)",
            "12:10-13:40 ТОИ (Спирина, пр 428-2)",
            "14:00-15:30 ЯП (лк 408-2)",
            "15:50-17:20 Физика (лабы, 422-3)",
            "17:40-19:10 Физика (лабы, 422-3)"
        ],
        "Четверг": [
            "10:20-11:50 История (пр 121-3)",
            "12:10-13:40 Электротехника (лк 508-3)",
            "14:00-15:30 Математика (пр 521-2)"
        ],
        "Пятница": [
            "8:30-10:00 Физкультура",
            "10:20-11:50 Физика (лк В-3)",
            "12:10-13:40 Электротехника (лабы 503-3)",
            "14:00-15:30 Электротехника (лабы 503-3)"
        ],
        "Суббота": [],
        "Воскресенье": []
    },
    "Знаменатель": {
        "Понедельник": [
            "8:30-10:00 Физика (пр, 425-3)",
            "10:20-11:50 Математика (пр 121-3)",
            "12:10-13:40 Математика (лк А-3)"
        ],
        "Вторник": [
            "8:30-10:00 Английский (пр 303а-1)",
            "10:20-11:50 Математика (лк 433-3)",
            "12:10-13:40 Физкультура",
            "14:00-15:30 ОИБ (лк 408-2)"
        ],
        "Среда": [
            "12:10-13:40 ТОИ (Спирина, пр 428-2)",
            "14:00-15:30 ЯП (лк 408-2)"
        ],
        "Четверг": [
            "8:30-10:00 История (лк Г-3)",
            "10:20-11:50 Электротехника (лк 508-3)",
            "12:10-13:40 ТОИ (Спирина, лк 408-2)",
            "14:00-15:30 Математика (пр 521-2)"
        ],
        "Пятница": [
            "8:30-10:00 Физкультура",
            "10:20-11:50 Физика (лк В-3)",
            "12:10-13:40 ЯП (лабы 427а-2)",
            "14:00-15:30 ЯП (лабы 427а-2)"
        ],
        "Суббота": [],
        "Воскресенье": []
    }
}

SCHEDULE_2 = {
    "Числитель": {
        "Понедельник": [
            "8:30-10:00 Физика (пр, 425-3)",
            "10:20-11:50 Математика (пр 121-3)",
            "12:10-13:40 Математика (лк А-3)",
            "14:00-15:30 История (лк А-3)"
        ],
        "Вторник": [
            "8:30-10:00 Английский (пр 303а-1)",
            "10:20-11:50 Математика (лк 433-3)",
            "12:10-13:40 Физкультура",
            "14:00-15:30 ОИБ (лк 408-2)"
        ],
        "Среда": [
            "12:10-13:40 ТОИ (Спирина, пр 428-2)",
            "14:00-15:30 ЯП (лк 408-2)",
            "15:50-17:20 Физика (лабы, 422-3)",
            "17:40-19:10 Физика (лабы, 422-3)"
        ],
        "Четверг": [
            "10:20-11:50 История (пр 121-3)",
            "12:10-13:40 Электротехника (лк 508-3)",
            "14:00-15:30 Математика (пр 521-2)"
        ],
        "Пятница": [
            "8:30-10:00 Физкультура",
            "10:20-11:50 Физика (лк В-3)",
            "12:10-13:40 ЯП (лабы 427а-2)",
            "14:00-15:30 ЯП (лабы 427а-2)"
        ],
        "Суббота": [],
        "Воскресенье": []
    },
    "Знаменатель": {
        "Понедельник": [
            "8:30-10:00 Физика (пр, 425-3)",
            "10:20-11:50 Математика (пр 121-3)",
            "12:10-13:40 Математика (лк А-3)"
        ],
        "Вторник": [
            "8:30-10:00 Английский (пр 303а-1)",
            "10:20-11:50 Математика (лк 433-3)",
            "12:10-13:40 Физкультура",
            "14:00-15:30 ОИБ (лк 408-2)"
        ],
        "Среда": [
            "10:20-11:50 ТОИ (Матвеева, лабы 428-2)",
            "12:10-13:40 ТОИ (Спирина, пр 428-2)",
            "14:00-15:30 ЯП (лк 408-2)"
        ],
        "Четверг": [
            "8:30-10:00 История (лк Г-3)",
            "10:20-11:50 Электротехника (лк 508-3)",
            "12:10-13:40 ТОИ (Спирина, лк 408-2)",
            "14:00-15:30 Математика (пр 521-2)"
        ],
        "Пятница": [
            "8:30-10:00 Физкультура",
            "10:20-11:50 Физика (лк В-3)",
            "12:10-13:40 Электротехника (лабы 503-3)",
            "14:00-15:30 Электротехника (лабы 503-3)"
        ],
        "Суббота": [],
        "Воскресенье": []
    }
}

RUSSIAN_DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


def get_today_schedule_1():
    today = datetime.date.today()
    delta_days = (today - START_DATE).days
    week_number = delta_days // 7
    week_type = "Знаменатель" if week_number % 2 == 0 else "Числитель"
    weekday_name = RUSSIAN_DAYS[today.weekday()]
    lessons = SCHEDULE_1[week_type].get(weekday_name, [])
    return lessons, week_type, weekday_name
def get_tomorrow_schedule_1():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    delta_days = (tomorrow - START_DATE).days
    week_number = delta_days // 7
    week_type = "Знаменатель" if week_number % 2 == 0 else "Числитель"
    weekday_name = RUSSIAN_DAYS[tomorrow.weekday()]
    lessons = SCHEDULE_1[week_type].get(weekday_name, [])
    return lessons, week_type, weekday_name

def get_today_schedule_2():
    today = datetime.date.today()
    delta_days = (today - START_DATE).days
    week_number = delta_days // 7
    week_type = "Знаменатель" if week_number % 2 == 0 else "Числитель"
    weekday_name = RUSSIAN_DAYS[today.weekday()]
    lessons = SCHEDULE_2[week_type].get(weekday_name, [])
    return lessons, week_type, weekday_name
def get_tomorrow_schedule_2():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    delta_days = (tomorrow - START_DATE).days
    week_number = delta_days // 7
    week_type = "Знаменатель" if week_number % 2 == 0 else "Числитель"
    weekday_name = RUSSIAN_DAYS[tomorrow.weekday()]
    lessons = SCHEDULE_2[week_type].get(weekday_name, [])
    return lessons, week_type, weekday_name

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помощник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.strip()

    if text == "👋 Поздороваться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 подгруппа")
        btn2 = types.KeyboardButton("2 подгруппа")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Выберите подгруппу", reply_markup=markup)
    elif text == "1 подгруппа":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Расписание на сегодня (1 подгруппа)")
        btn2 = types.KeyboardButton("Расписание на завтра (1 подгруппа)")
        btn3 = types.KeyboardButton('Полное расписание')
        btn4 = types.KeyboardButton('Перезапустить бота')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Вы в 1 подгруппе", reply_markup=markup)
    elif text == "Расписание на сегодня (1 подгруппа)":
        lessons, week_type, weekday = get_today_schedule_1()
        if lessons:
            msg = f"📅 Сегодня {weekday} ({week_type})\n\n"
            msg += "\n".join(f"{i + 1}. {lesson}" for i, lesson in enumerate(lessons))
        else:
            msg = f"📅 Сегодня {weekday} ({week_type})\n\n🎉 Пар нет! Отдыхай!"
        bot.send_message(message.from_user.id, msg)
    elif text == "Расписание на завтра (1 подгруппа)":
        lessons, week_type, weekday = get_tomorrow_schedule_1()
        if lessons:
            msg = f"📅 Завтра {weekday} ({week_type})\n\n"
            msg += "\n".join(f"{i + 1}. {lesson}" for i, lesson in enumerate(lessons))
        else:
            msg = f"📅 Завтра {weekday} ({week_type})\n\n🎉 Пар нет! Отдыхай!"
        bot.send_message(message.from_user.id, msg)


    elif text == "2 подгруппа":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Расписание на сегодня (2 подгруппа)")
        btn2 = types.KeyboardButton("Расписание на завтра (2 подгруппа)")
        btn3 = types.KeyboardButton('Полное расписание')
        btn4 = types.KeyboardButton('Перезапустить бота')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Вы во 2 подгруппе", reply_markup=markup)
    elif text == 'Перезапустить бота':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помощник!", reply_markup=markup)
    elif text == "Расписание на сегодня (2 подгруппа)":
        lessons, week_type, weekday = get_today_schedule_2()
        if lessons:
            msg = f"📅 Сегодня {weekday} ({week_type})\n\n"
            msg += "\n".join(f"{i + 1}. {lesson}" for i, lesson in enumerate(lessons))
        else:
            msg = f"📅 Сегодня {weekday} ({week_type})\n\n🎉 Пар нет! Отдыхай!"
        bot.send_message(message.from_user.id, msg)
    elif text == "Расписание на завтра (2 подгруппа)":
        lessons, week_type, weekday = get_tomorrow_schedule_2()
        if lessons:
            msg = f"📅 Завтра {weekday} ({week_type})\n\n"
            msg += "\n".join(f"{i + 1}. {lesson}" for i, lesson in enumerate(lessons))
        else:
            msg = f"📅 Завтра {weekday} ({week_type})\n\n🎉 Пар нет! Отдыхай!"
        bot.send_message(message.from_user.id, msg)


    elif text == "dr":
        bot.send_message(message.from_user.id, "Илюха Краснов С Днем Рождения🎉❤️🎂")
    elif text == "Рандомайзер":
        bot.send_message(message.from_user.id, f"🎲 Кинул кубик: {random.randint(1, 21)}")
    elif text == "Полное расписание":
        bot.send_message(message.from_user.id, "https://postimg.cc/CBhb0xRq")
    else:
        bot.send_message(message.from_user.id, "Не понял команду. Нажми на кнопку!")


if __name__ == "__main__":

    bot.polling(none_stop=True)





