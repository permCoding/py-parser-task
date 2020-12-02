import module as m
import datetime as dt


bs = m.get_txt()

t_scores = bs.find('table', class_="t_scores")
t_body = t_scores.find('tbody')
list_tr = t_body.find_all('tr')

results = []
for tr in list_tr:
    list_td = tr.find_all('td')
    list_td[1] = tr.find('td', class_='team').find('i')
    list_td = [td.contents[0] for td in list_td]
    results.append(list_td)

# results.sort(key=lambda item: int(item[6]), reverse=True) # по забитым

results.sort(
    key=lambda item: (-int(item[3]), -int(item[6]))
    )

for line in results:
    # print(' '.join(line))
    s = '{0:4s}{1:14s}{2:4s}{3:4s}'.format(line[0],line[1],line[3],line[6])
    print(s)
