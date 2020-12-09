import requests, lxml
from bs4 import BeautifulSoup


def get_txt(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'
    }
    txt = requests.get(url, headers=head).text  # получить содержимое страницы в виде строки
    return BeautifulSoup(txt, 'lxml')  # вернуть в виде объекта BS


def save_html(url):
    soup = get_txt(url)
    t_body = soup.find('tbody')
    list_tr = t_body.find_all('tr')
    f = open('index.html', 'w', encoding='utf-8')
    f.write(str(list_tr))
    f.close()


def get_list_tr():
    f = open('index.html', 'r')
    html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    list_tr = soup.find_all('tr')
    f.close()
    return list_tr


def print_results(results):
    f = open('results.txt', 'w')
    for line in results:
        # f'% % % %' % (line[0], line[1], line[2], line[3])
        f.write('{} {} {} {}\n'.format(line[0], line[1], line[2], line[3]))
    f.close()
