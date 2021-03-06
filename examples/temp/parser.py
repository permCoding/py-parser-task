import module as m


url = 'https://www.championat.com/football/_england/tournament/4013/table/'

# m.save_html(url)

list_tr = m.get_list_tr()

results = []
for tr in list_tr:
    list_td = tr.find_all('td')
    order = 3  # место
    name = 'Name'  # название

    balls = list_td[6].find_all('span')
    ball_z = int(balls[0].contents[0])  # забитых
    ball_p = int(balls[2].contents[0])  # пропущенных

    rec = [order, name, ball_z, ball_p]
    results.append(rec)

m.print_results(results)
