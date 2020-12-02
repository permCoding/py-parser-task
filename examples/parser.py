import module as m


bs = m.get_txt('https://russianfootballtable.ru/')

t_body = bs.find('tbody')
list_tr = t_body.find_all('tr')

results = []
for tr in list_tr:
    list_td = tr.find_all('td')
    list_td[1] = tr.find('td', class_='team').find('i')
    list_td = [td.contents[0] for td in list_td]
    results.append(list_td)

for rec in results:
    print(' '.join(rec))
