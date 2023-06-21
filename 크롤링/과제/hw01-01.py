
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_weather_find(html):

    print('[find 함수 사용]')
    seven_day = html.find(id = 'seven-day-forecast-container')
    tombstone = seven_day.find_all(class_ ='tombstone-container')
    print('tomestone-container 검색 개수: ', len(tombstone))


    for i in tombstone:
        
        period = i.find('p', {'class': 'priod-name'}).text
        img_desc = i.find('img')['title']
        temp = i.find('p', {'class': 'temp'}).text #temp 혹은 temp tmep-low 로 적어됨
        short_desc = i.find('p', {'class': 'short-desc'}).text
       # print(li.find('p', {'class': 'temp'}),'[temp: ]', i) #temp 혹은 temp tmep-low 를 다 적어도 된다.
        #print(li.find('p', img['title']))

        print('-'*50)
        #print(html.find('p', {'class': 'priod-name'}).get_text())
        #print(period.get_text())
        print('[Period]:{0}'.format(period))
        print('[img_desc]:{0}'.format(img_desc))
        print('[temp]:{0}'.format(temp))
        print('[short_desc]:{0}'.format(short_desc))


def get_weather_select(html):

    print('\n')
    print('[select 함수 사용]')
    seven_day = html.select_one('div #seven-day-forecast-container')
    tombstone = seven_day.select('.tombstone-container')
    print('tomestone-container 검색 개수: ', len(tombstone))


    for i in tombstone:
        
        period = i.select_one('.priod-name')
        img_desc = i.select_one('img')['title']
        temp = i.select_one('.temp').text #temp 혹은 temp tmep-low 로 적어됨
        short_desc = i.select_one('.short-desc').text
       # print(li.find('p', {'class': 'temp'}),'[temp: ]', i) #temp 혹은 temp tmep-low 를 다 적어도 된다.
        #print(li.find('p', img['title']))

        print('-'*50)
        #print(html.find('p', {'class': 'priod-name'}).get_text())
        #print(period.get_text())
        print('[Period]:{0}'.format(period))
        print('[img_desc]:{0}'.format(img_desc))
        print('[temp]:{0}'.format(temp))
        print('[short_desc]:{0}'.format(short_desc))

#tag4 = li_text.find('p', {'img': 'alt'})


#values = list(li_text.attrs.values())


#    try:
#        link_tag = ul_len.find_all('p', {'class': ['period-name, short desc, temp temp-low, temp temp-high']})
#    except temp temp-low as e:
#        return None
        



#try:
#    link_tag = ul_len.find_all('p', {'class': ['period-name, short desc, temp temp-low, temp temp-high']})
#except temp temp-low as e:
#    return None


#sql 함수 과제 참고


def main():

    page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY')
    html = BeautifulSoup(page.read(), 'html.parser')

    print('National Weather Service Scraping')
    print('-'*50)

    get_weather_find(html)
    get_weather_select(html)

main()