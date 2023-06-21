from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url = 'https://finance.naver.com/sise/sise_market_sum.naver'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')


while True:
    topten = soup.select('td > a.tltle')         #기업 정보 크롤링
    #print(topten)                                #기업 정보 리스트 담기
    print('-'*35)
    print('[네이버 코스피 상위 10대 기업 목록]')
    print('-'*35)

    for i in range(10):
        print(f'[{i+1:2}] {topten[i].text}') # 상위 10대 기업 출력
    try:
        n = int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
        if n == -1:                         # -1 입력 시 종료
            print('프로그램을 종료합니다.')
            break                           
    except:
        print('1~10까지의 수를 입력하세요(-1: 종료)')  


    link = 'https://finance.naver.com/' + topten[i]['href']
    html = requests.get(link)
    soup = BeautifulSoup(html.text, 'html.parser')
    topten_info = soup.select('dl.blind > dd')  # 종목 상세 정보 크롤링
    # print(topten_info)                  # 종목 상세 정보 리스트 담기 
    print(topten_info[1].text)            # 종목명
    print(topten_info[2].text)            # 종목코드
    print(topten_info[3].text)            # 현재가/전일대비/퍼센트/전일가
    print(topten_info[4].text)            # 시신가
    print(topten_info[5].text)            # 고가
    print(topten_info[7].text)            # 저가
