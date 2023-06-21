    # work_12_29_이아름
# ===================================================================
# 1. 계산기 프로그램을 클래스기반으로 만들어 주십시오. 
#  - 정수, 실수 계산
#  - 덧셈, 뺄셈
# ===================================================================

#data = input("연산할 숫자를 입력해주세요(ex. 3 + 4 - 2 = ) : ")
    
class Calu:
    def __init__(self, *num):
        self.num = num

    def add(self, *other):
        return sum(self.num) + sum(other)
    
    def extract(self, *other):
        self.result = self.num[0]
        for n in range(1, len(self.num)):
            self.result -= self.num[n]
        for n in range(len(other)):
            self.result -= other[n]
        return round(self.result, 3)


    
a = Calu(1.5, 8, -3)
print(a.add())
print(a.extract())




# ===========================================================================
# 2. 함수 구현
#   2-1) 구구단 2~9단 출력 반복문 1개
#   2-2) 2-1을 list 컨플리헨션 구현하기 (X)
#   3-3) 별자리, 띠
#    - 12간지 순서: 원숭이, 닭, 개, 돼지, 쥐, 소, 호랑이, 토끼, 용, 뱀, 말, 양
#    -  1월 20일 ~  2월 18일 : 물병자리   2월 19일 ~  3월 20일 : 물고기자리
#       3월 21일 ~  4월 19일 : 양자리     4월 20일 ~  5월 20일 : 황소자리
#       5월 21일 ~  6월 21일 : 쌍둥이자리 6월 22일 ~  7월 22일 : 게자리
#       7월 23일 ~  8월 22일 : 사자자리   8월 23일 ~  9월 23일 : 처녀자리
#       9월 24일 ~ 10월 22일 : 천칭자리  10월 23일 ~ 11월 22일 : 전갈자리
#      11월 23일 ~ 12월 24일 : 궁수자리  12월 25일 ~  1월 19일 : 염소자리
# ===========================================================================
# [2-1]
def mul(start, end):
    dan, i = start, 0
    while True:
        if i == 0:
            if dan < end:
                print(f'--[{dan}단]--', end = '\t')
                dan += 1
            elif dan == end: 
                print(f'--[{dan}단]--')
                dan, i = start, 1
        elif i < 10:
            if dan < end:
                print(f'{dan} * {i:>2} = {dan * i:>2}', end = '\t')
                dan += 1
            elif dan == end: 
                print(f'{dan} * {i:>2} = {dan * i:>2}')
                i += 1
                dan = start
        else: break

mul(2, 9)



# [2-3]
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
    my_zoo = zoo[year%12] #12로 나눠서 나온 값으로 인덱스 위치의 값이 출력됨

    m_d = [120, 219, 321, 420, 521, 622, 723, 823, 924, 1023, 1123, 1225]
    star = ['물병자리', '물고기자리', '양자리', '황소자리', '쌍둥이자리', '게자리', '사자자리', '처녀자리', '천징자리', '전갈자리', '궁수자리', '염소자리']
    for n in range(len(m_d)):
        if int(num[2:6]) > 1231:
            print("주민번호가 정확하지 않습니다")
        elif monthday >= m_d[n] :
            my_star = star[n]
        elif monthday < m_d[0]:
            my_star = star[-1]
       

    return my_zoo, my_star

my = '932202-2000000'
print(zoo_star(my))