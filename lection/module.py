import requests, lxml
from bs4 import BeautifulSoup

def get_bs(url):
	head = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
	}
	txt = requests.get(url, headers=head).text
	return BeautifulSoup(txt, 'lxml')