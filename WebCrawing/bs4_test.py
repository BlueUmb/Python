from bs4 import BeautifulSoup

html = open('fruits.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one('body') #객체.select_one(<선택자>) : css 선택자로 요소 하나를 추출함
ptag = body.find('p')

print('1번째 ptag 출력 : ', ptag)
print('1번째 ptage : ', ptag['class'])

ptag['class'][1] = 'white'
print('1번째 ptage : ', ptag['class'])

ptag['id'] = 'apple'
print('1번째 p태그의 id속성 : ', ptag['id'])

print()
body_tag = soup.find('body')
print(body_tag)


print()
idx = 0
print('children 속성으로 하위 항목 보기')
for child in body_tag.children:
    idx += 1
    print(str(idx) + ' 번째 요소 : ', child)

print()
mydiv = soup.find('div')
print(mydiv)

print()

print('div 태그의 부모 태그는?')
print(mydiv.parent)

print()
print('mydiv 태그의 모든 상위 부모 태그들의 이름 : ')
parents = mydiv.findParents
for p in parents:
    print(p.name)