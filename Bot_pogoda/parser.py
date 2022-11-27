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

def probki():
    url = "http://www.probki-online.ru/probki-online.php?city=rostov-na-donu"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    info = soup.find('ymaps', class_="ymaps-2-1-79-float-button-text").get_text()
    answer = f"Пробки(балл): {info}"
    return answer
print(probki())