
import requests
from bs4 import BeautifulSoup

#requests 로 url 사용 시 한글 깨짐 오류 현상이 나타나지 않는다, utf-8 인코딩하여 넘겨준다. 
#subject = list()
#def weather_ifo():
    
html = requests.get('https://search.naver.com/search.naver?query=대구+날씨')
bs = BeautifulSoup(html.text, 'html.parser')

loc = bs.find('div', {'class': 'title_area _area_panel'})
loc_tit = loc.find('h2', {'class':'title'}).text
loc_tem = bs.find('div', {'class' : 'temperature_text'}).text
loc_wea = bs.find('span', {'class' : 'weather'}).text
loc_air = bs.find('ul', {'class' : 'today_chart_list'})
loc_air_info = bs.find_all('li', {'class': 'itme_today'})

#loc_houlry_wea = bs.find('div', {'class' : 'graph_inner _hourly_weather'})

weather_time = bs.find_all('li', {'class': '_li'})

print('현재 위치: ', loc_tit)
print('현재 온도: ', loc_tem)
print('날씨 상태: ', loc_wea)
print('공기 상태: ', loc_air_info)


print('-'*20)
print('시간대별 날씨 및 온도')
print('-'*20)
for i in weather_time:
    print(i.text)




#https://blog.naver.com/bbaeng_du/222984433581


