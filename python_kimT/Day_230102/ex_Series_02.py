# 모듈 로딩 --------------------------------------------------

import pandas as pd                 # 데이터분석용 패키지
import ex_pandas as mp   # 나의 모듈 Day_230102\ex_pandas.py

# ----------------------------------------------------------------------------------------------------
# Series 객체의 요소 다루기 => 인덱스 사용
# [사용법] 객체변수명[인덱스]
# ----------------------------------------------------------------------------------------------------
data = list(range(5, 31, 5))
sr1=pd.Series(data)

# 요소 읽기
print(f'sr1[0] => {sr1[0]}')
print(f'sr1[1] => {sr1[5]}')

# for idx in range(len(sr1)):
#     print(f'sr1[{idx}] => sr1[{idx}]')

for idx in sr1.index:
    print(f'idx => {idx}')
    print(f'sr1[{idx}] => sr1[{idx}] : {type(sr1[idx])}')


# 요소 여러개 읽기 = > 변수명[인데스1, 인덱스2]----------------------------------------------------------------------
# ==> 결과 데이터 시리즈(Series) 타입
print(f'srl[[0,4]] => \n{sr1[[0, 4]]}\n{type(sr1[[0,4]])}')
print(f'srl[[4]]   => \n{sr1[[4]]}\n{type(sr1[[4]])}')
#print(f'srl[[0,1,2,3,4]] => \n{sr1[[0,1,2,3, 4]]}\n{type(sr1[[0,1,2,3,4]])}')

#요소 범위지정하여 읽기 => 변수명[ 시작 : 끝인덱스 +1] (끝번호를 포함하지 않기 때문에)

print(f'sr1[] => \n{sr1[0:5]}n{type(sr1[0:5])}')
print(f'sr1[] => \n{sr1[0:5:2]}n{type(sr1[0:5:2])}') #=> 짝수만 뽑음



import pandas as pd               

# ----------------------------------------------------------------------------------------------------
# Series 객체의 요소 다루기 => 인덱스 사용
# [사용법] 객체변수명[인덱스]
# ----------------------------------------------------------------------------------------------------
import pandas as pd               

data = list(range(1, 31))
pd.Series(data)


import random as r
for _ in range(30):
    print(r.randint(1, 100), end = ' ')