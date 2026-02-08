import os
import datetime
import telebot
import threading
import http.server
import socketserver
from telebot import types

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

SCHEDULE = {
    "Числитель": {
        "Понедельник": [
            "Физика (пр, 425-3)",
            "Математика (121-3)",
            "Математика (А-3)",
            "История (А-3)"
        ],
        "Вторник": [
            "Английский (303а-1)",
            "Математика (433-3)",
            "Физкультура",
            "ОИБ (408-2)"
        ],
        "Среда": [
            "ТОИ (Спирина, 428-2)",
            "ЯП (408-2)",
            "Физика (лабы, 422-3)",
            "Физика (лабы, 422-3)"
        ],
        "Четверг": [
            "История (121-3)",
            "Электротехника (508-3)",
            "Математика (521-2)"
        ],
        "Пятница": [
            "Физкультура",
            "Физика (В-3)",
            "ЯП (427а-2)",
            "ЯП (427а-2)"
        ],
        "Суббота": [],
        "Воскресенье": []
    },
    "Знаменатель": {
        "Понедельник": [
            "Физика (пр, 425-3)",
            "Математика (121-3)",
            "Математика (А-3)"
        ],
        "Вторник": [
            "Английский (303а-1)",
            "Математика (433-3)",
            "Физкультура",
            "ОИБ (408-2)"
        ],
        "Среда": [
            "ТОИ (Матвеева, 428-2)",
            "ТОИ (Спирина, 428-2)",
            "ЯП (408-2)"
        ],
        "Четверг": [
            "История (Г-3)",
            "Электротехника (508-3)",
            "ТОИ (Спирина, 408-2)",
            "Математика (521-2)"
        ],
        "Пятница": [
            "Физкультура",
            "Физика (В-3)",
            "Электротехника (503-3)",
            "Электротехника (503-3)"
        ],
        "Суббота": [],
        "Воскресенье": []
    }
}

RUSSIAN_DAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

def get_today_schedule():

    today = datetime.date.today()
    delta_days = (today - START_DATE).days
    week_number = delta_days // 7
    week_type = "Знаменатель" if week_number % 2 == 0 else "Числитель"
    weekday_name = RUSSIAN_DAYS[today.weekday()]
    lessons = SCHEDULE[week_type].get(weekday_name, [])
    return lessons, week_type, weekday_name

bot = telebot.TeleBot(BOT_TOKEN)

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
        btn1 = types.KeyboardButton("Скинь расписание")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Чем могу помочь?", reply_markup=markup)

    elif text == "Скинь расписание":
        lessons, week_type, weekday = get_today_schedule()
        if lessons:
            msg = f"📅 Сегодня {weekday} ({week_type})\n\n"
            msg += "\n".join(f"{i+1}. {lesson}" for i, lesson in enumerate(lessons))
        else:
            msg = f"📅 Сегодня {weekday} ({week_type})\n\n🎉 Пар нет! Отдыхай!"
        bot.send_message(message.from_user.id, msg)

    elif text == "dr":
        bot.send_message(message.from_user.id, "Илюха Краснов С Днем Рождения<3")

    else:
        bot.send_message(message.from_user.id, "Не понял команду. Нажми на кнопку!")

if __name__ == "__main__":

    bot.polling(none_stop=True)
