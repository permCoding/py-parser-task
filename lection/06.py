import module6 as m

url = 'https://russianfootballtable.ru/'
bs = m.get_bs(url)

# table = bs.find('table', class_='t_scores')
# tbody = table.find('tbody')

tbody = bs.find('tbody')
list_tr = tbody.find_all('tr')
rows_content = []
for tr in list_tr:
    list_td = tr.find_all('td')
    list_td[1] = list_td[1].find('i')
    list_td = [td.contents[0] for td in list_td]
    rows_content.append(list_td)

# rows_content.sort(key=lambda item: item[1])
# rows_content.sort(key=lambda item: -int(item[6]))
rows_content.sort(key=lambda item: int(item[6]), reverse=True)

for item in rows_content:
    print(item[0], item[1], item[2], item[3], item[6])


# print(rows_content)
# print(rows_content[0][2].contents[0])
