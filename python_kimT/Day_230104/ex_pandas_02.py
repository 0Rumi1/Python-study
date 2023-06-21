# -----------------------------------------------------------------------------
# 데이터 분석 => 통계 함수들, 고유값, 결측치
# -----------------------------------------------------------------------------
# row = instance = entry

import pandas as pd

FILE = r'Day_230103\dataFiles-20230103T063952Z-001\dataFiles\auto-mpg.csv'

# 데이터 정보 확인 함수
def printDataIno(df):
    df.info()  # 실수로 보여지지만, object(문자) 형식이다.
    print(df.head(), df.tail(), sep='\n', end='\n\n')
    print(df.describe(), end= '\n\n')
    print(f'index = {df.index}\nColumns => {df.columns}', end= '\n\n')

# (1) FILE => DataFrame 읽기
mpgDF = pd.read_csv(FILE, header=None) # header 로 추출 시, 칼럼명이 아니라 데이터 이다. 따라서, None 으로 지정


# (2) 데이터 정보 확인
printDataIno(mpgDF)

# (3) 컬럼명 추가
# 'mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name'
mpgDF.columns =['mpg', 'cylinders' ,'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']
print(mpgDF.head(3))

# (4) 실제 데이터와 타입이 맞지 않는 데이터 처리
# horsepower 데이터 값 중에 '?' 으로 오류 발생함
# (4-1) 해당 컬럼에 데이터 종류 확인 => 고윳값 unique()
horseUnique = mpgDF.horsepower.unique()
print("horsepower dtypes :", horseUnique)


# (4-2) 해당 컬럼에 데이터 종류별 갯수확인 => value_counts()
horseUniqueCounts=mpgDF.horsepower.value_counts()
print("horseUniqueCounts : ", horseUniqueCounts, type(horseUniqueCounts))

print(horseUniqueCounts['?'])


# print("horsepower dtypes :", mpgDF.horsepower.dtype)

# mpgDF.horsepower.astype('float64')
# print("horsepower dtypes :", mpgDF.horsepower.dtype)

# print(mpgDF.info)