'''
    * 네이버 웹툰 페이지 크롤링 (bs4)
        - 요일별 폴더에 각각의 이미지를 다운로드
        - 타이틀번호, 요일, 제목, 링크 내용으로 CSV 파일 생성

    * 크롤링 순서
        <div class="thumb">인 항목을 추출함
        반복문 사용
            <a> 태그의 href 속성을 읽어 옴
                replace()
                split()
            <img> 태그
                title 속성을 읽어와서 제목으로 처리함

        리스트에 추가함
        해당 이미지를 각 요일 폴더에 이미지로 저장함

        데이터 프레임 만들어 CSV 파일로 저장함
'''

import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday'
response = urlopen(myurl)

soup = BeautifulSoup(response, myparser)
weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}

myfolder = 'c:\\Users\\kidwa\\OneDrive\\바탕 화면\\ezen_webtoon\\'

try:
    if not os.path.exists(myfolder):
        os.mkdir(myfolder)

    for mydir in weekday_dict.values():
        mypath = myfolder + mydir

        if not os.path.exists(mypath):
            os.mkdir(mypath)

except FileExistsError as err:
    pass

'''
    save_file(): 웹 페이지에 존재하는 이미지를 로컬 컴퓨터에 저장하기 위한 함수
                 <img src=''>는 웹 페이지에 존재하는 이미지 경로임
                 'mon', 'thu' 등 요일 정보 저장
'''


def save_file(mysrc, myweekday, mytitle):
    image_file = urlopen(mysrc)
    file_name = myfolder + myweekday + '\\' + mytitle + '.jpg'
    
    myfile = open(file_name, mode='wb')
    myfile.write(image_file.read())

mylist = []
mytarget = soup.find_all('div', attrs={'class':'thumb'})
print('만화의 총 개수 : '+str(len(mytarget)))
for naver_webtoon_source in mytarget:
    myhref = naver_webtoon_source.find('a').attrs['href']
    myhref = myhref.replace('/webtoon/list?', '')
    result = myhref.split('&')
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split("=")[1]
    myweekday = weekday_dict[myweekday]
    # print(mytitleid+'/'+myweekday)

    imgtag = naver_webtoon_source.find('img')
    mysrc = imgtag.attrs['src']
    mytitle = imgtag.attrs['title'].strip()

    mytuple = tuple([mytitleid,myweekday,mytitle,mysrc])
    mylist.append(mytuple)

print(mylist)

myframe = DataFrame(mylist, columns=['타이틀 번호','요일','제목','링크'])
filename = 'cartoon.csv'

myframe.to_csv(filename,encoding='utf-8',index=False)
print(filename+"파일로 저장됨")
print('\n finished')
