import requests, lxml
from bs4 import BeautifulSoup


def get_txt(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'
    }
    txt = requests.get(url, headers=head).text  # получить содержимое страницы в виде строки
    return BeautifulSoup(txt, 'lxml')  # вернуть в виде объекта BS
