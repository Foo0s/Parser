import requests
from bs4 import BeautifulSoup
def parser():
    url = "https://pogoda.mail.ru/prognoz/rostov-na-donu/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    day = soup.find("div", class_="information__header__left__date").get_text().lstrip().rstrip()
    gradys = soup.find("div", class_="information__content__temperature").get_text().lstrip().rstrip()
    oshyt = soup.find("div", class_="information__content__additional__item").get_text().lstrip().rstrip()
    dop = soup.find("div", class_="information__content__additional information__content__additional_first").get_text().lstrip().rstrip()
    answer = f"День: {day}\nПогода: {gradys}\nДругая информация: {oshyt}\nДоп: {dop}"
    return answer
