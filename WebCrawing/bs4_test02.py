from bs4 import BeautifulSoup

myencoding = "utf-8"
myparser = 'html.parser'
filename = 'cartoon.html'

html = open(filename, encoding=myencoding)
soup = BeautifulSoup(html, myparser)

h1 = soup.select_one("div#cartoon > h1").string
print("h1 :", h1)

li = soup.select("div#cartoon > ul#element > li")
list_li = []
for i in range(len(li)):
    list_li.append(li[i].string)

print("li :",list_li)
print('-' * 30)
choice = lambda x : print(soup.select_one(x).string)

print('\nchoice("#item5) : ',end='')
choice("#item5")

print('\nchoice("li#item4) : ',end='')
choice("li#item4")

print('\nchoice("ul > li#item3) : ',end='')
choice("ul > li#item3")

print('\nchoice("#itemlist #item2) : ',end='')
choice("#itemlist #item2")

print()
print('\nsoup.select("li")[1].string : ', end='')
print(soup.select("li")[1].string)

# find_all(tag, attributes, limit = 숫자) : 조건에 맞는 HTML 태그를 전부 찾아줌
print('\nsoup.find_all("li")[3].string : ', end='')
print(soup.find_all("li")[3].string)

print('-' * 30)

# class 속성이 us인 1번째 요소
print(soup.select("#vegetables > li[class='us']")[0].string)
print(soup.select("#vegetables > li.us")[1].string)

print()

# ^= : ~으로 시작하는, $= : ~으로 끝나는
result = soup.select('a[href$=".com"]')
for item in result:
    print(item['href'])

print()
# *= : ~을 포함하고 있는
result = soup.select('a[href*="aum"]')
for item in result:
    print(item['href'])
