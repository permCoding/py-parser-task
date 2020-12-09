import module as m


url = 'https://www.championat.com/football/_england/tournament/4013/table/'

# m.save_html(url)

list_tr = m.get_list_tr()

results = []
for tr in list_tr:
    list_td = tr.find_all('td')
    order = 4  # место
    name = 'Name'  # название
    ball_z = 19  # забитых
    ball_p = 10  # пропущенных
    rec = [order, name, ball_z, ball_p]
    results.append(rec)

m.print_results(results)
