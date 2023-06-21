
'''데이터크롤링과 정제
과제 #1

National Weather Service 웹사이트 (샌프란시스코 지역)
- https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

def parse_use_find(html):
    '''
    find() 함수를 사용하여 html  내용을 크롤링
    :param html:
    :return:
    '''
    print('[find 함수 사용]')
    
    seven_day = html.find(id='seven-day-forecast-container')
    forecast_items = seven_day.find_all(class_='tombstone-container')
    print('총 tomestone-container 검색 개수: ', len(forecast_items))

    for day in forecast_items:             
        period = day.find('p', {'class' : 'period-name'}).text
        img_desc = day.find('img')['title'] # img의 'title' 속성값 가져오기
        short_desc = day.find('p', class_='short-desc').text
        temp = day.find('p', class_='temp').text
            
        print('-' * 80)
        print('[Period]: {0}'.format(period))
        print('[Short desc]:  {0}'.format(short_desc))
        print('[Temperature]: {0}'.format(temp))
        print('[Image desc]: {0}'.format(img_desc))
        
    print('-' * 80)

def parse_use_select(html):
    '''
    select 함수를 사용하여 html 내용을 크롤링
    '''
    print('[select 함수 사용]')
    seven_day = html.select_one('div #seven-day-forecast-container')
    forecast_items = seven_day.select('.tombstone-container')
    print('총 tomestone-container 검색 개수: ', len(forecast_items))

    for day in forecast_items:        
        period = day.select_one('.period-name').text
        img_desc = day.select_one('img')['title']
        short_desc = day.select_one('.short-desc').text
        temp = day.select_one('.temp').text
        # img의 'title' 속성값 가져오기
        
        print('-' * 80)
        print('[Period]: {0}'.format(period))
        print('[Short desc]:  {0}'.format(short_desc))
        print('[Temperature]: {0}'.format(temp))
        print('[Image desc]: {0}'.format(img_desc))

def main():
    page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    html = BeautifulSoup(page.read(), 'html.parser')

    print('National Weather Service Scraping')
    print('----------------------------------')

    parse_use_find(html)
    parse_use_select(html)

main()
