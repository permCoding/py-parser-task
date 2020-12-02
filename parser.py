import module as m
import datetime as dt


bs = m.get_txt()
# print(bs.prettify())

t_scores = bs.find('table', class_="t_scores")
# print(t_scores)

t_body = t_scores.find('tbody')
# print(t_body)

list_tr = t_body.find_all('tr')
# print(list_tr[0])

data = list_tr[0]
print(data)
# num = data.find('td', class_='number')
# num = num.contents[0]
# print(num)

list_td = data.find_all('td')
# for td in list_td:
# 	print(td.contents[0])

# name = data.find('td', class_='team').find('i').contents[0]
# print(name)

list_td[1] = data.find('td', class_='team').find('i')
for td in list_td:
	print(td.contents[0])



# lines = []

# title = bs.find('h1', class_='channel-header__text').contents[0]
# lines.append(title)

# list_li = bs.find_all('li', class_='channel-schedule__event')
# for li in list_li:
# 	time = li.find('time', class_='channel-schedule__time').contents[0]
# 	name = li.find('span', class_='channel-schedule__text').contents[0]
# 	line = '%s\t%s' % (time, name)
# 	lines.append(line)

# result = '\n'.join(lines)

# print(result) # для контроля на экран
# print_result("bs_result.txt", result)


# tags_time = bs.find_all('time', class_='channel-schedule__time')
# times = []
# for t in tags_time:
# 	times.append(t.contents[0])
# print(times)

# tags_text = bs.find_all('span', class_='channel-schedule__text')
# texts = []
# for t in tags_text:
# 	texts.append(t.contents[0])
# print(texts)

# lines = list(zip(times, texts))

# for line in lines:
# 	print(line)