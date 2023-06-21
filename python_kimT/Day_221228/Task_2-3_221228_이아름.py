#별자리, 띠
#날짜가 작거나 같으면 월 그대로 > 별자리와 띠 출력
#starIdx = month if starDates[month]<=day else month-1 

def birth(num):
    n = int(num[7])
    if n in [1, 2]:
        year = int('19' + num[:2])
    elif n in [3, 4]: 
        year = int('20' + num[:2])
    month_day = int(num[2:6])
    return year, month_day

def zoo_star(num):
    year, monthday = birth(num)

    zoo = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양']
    my_zoo = zoo[year%12]

    m_d = [120, 219, 321, 420, 521, 622, 723, 823, 924, 1023, 1123, 1225]
    star = ['물병자리', '물고기자리', '양자리', '황소자리', '쌍둥이자리', '게자리', '사자자리', '처녀자리', '천징자리', '전갈자리', '궁수자리', '염소자리']
    for n in range(len(m_d)):
        if monthday >= m_d[n]:
            my_star = star[n]
        elif monthday < m_d[0]:
            my_star = star[-1]

    return my_zoo, my_star

my = '931202-2000000'
print(zoo_star(my))