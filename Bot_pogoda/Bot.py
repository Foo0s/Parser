import telebot
import parser
import time

token = "5844489105:AAFHieG0hbdl2MOOdgGspWF17biJdF2Mq2s"
list_2 = []
list_1 = ["Команда - start -> выводит основную информацию.",
          "команда pogoda-погода, выводит информацию о текущей погоде",
          "Вывод всех ваших записей -> /top",
          "Всё!"]

dnsbot = telebot.TeleBot(token)

@dnsbot.message_handler(commands=["start"])
def start(message):
    dnsbot.send_photo(message.chat.id,
                      "https://phonoteka.org/uploads/posts/2021-05/1621830237_7-phonoteka_org-p-anime-fon-geimer-7.jpg")
    dnsbot.send_message(message.chat.id, f"Приветствую, {message.from_user.first_name}, я бот-парсер, который выдаёт"
                                         f" различную информацию")
    dnsbot.send_message(message.chat.id, "Команда /help расскажет тебе о моём функционале.")

@dnsbot.message_handler(commands=["help"])
def help(message):
    dnsbot.send_message(message.chat.id, "Список моих возможностей...")
    for i in list_1:
        dnsbot.send_message(message.chat.id, i)
        time.sleep(0.8)

@dnsbot.message_handler(commands=["top"])
def top(message):
    for i in list_2:
        dnsbot.send_message(message.chat.id, i)

@dnsbot.message_handler(commands=["pogoda", "погода"])
def send_info(message):
    dnsbot.send_photo(message.chat.id, "https://phonoteka.org/uploads/posts/2021-05/1622249750_24-phonoteka_org-p-anime-art-paren-pod-dozhdem-krasivo-28.jpg")
    dnsbot.send_message(message.chat.id, parser.parser())

@dnsbot.message_handler(content_types=["text"])
def save_message(message):
    list_2.append(message.text)
    dnsbot.send_message(message.chat.id, "Ваше сообщение было добавлено в список!Чтобы его просмотреть введите команду /top")

dnsbot.polling(none_stop=True)
