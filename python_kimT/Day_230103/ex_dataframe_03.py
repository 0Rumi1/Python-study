#================================================================================
# DataFrame & Series 다루기 => 삭제
#================================================================================

# 모듈 로딩
import pandas as pd

# DF 객체 생성
df1=pd.DataFrame({'name':['마징가', '베트맨', '원더우먼'],
                    'kor': [87,97,69],
                    'eng': [99,73,89],
                    'sci': [71,95,62]})


# DF 데이터 확인하기
print(f'df1 ==========================> \n{df1}')
print(f'df1. index ==> \n{df1.index}')
print(f'df1. columns ==> \n{df1.columns}')

# 행(row, 가로 데이터) 삭제 => drop(메서드) ===================================
# '베트맨'이 있는 가로 라인 데이터 삭제\
# - inplace = False : 원본 데이터 적용 여부
#             결과 DataFrame 반환
# - inplace = True  : 원본 데이터 적용
#             None 반환 

# 원본은 변경되지 않고 복사본을 가져와 삭제한다.
retDF=df1.drop(1)
print(f'df1 ==========================> \n{retDF}')
print(f'df1 ==========================> \n{df1}')

#retDF 에서 2번 인덱스 행(row) 삭제 및 원본 적용
ret= retDF.drop(2, inplace=True)

print(f'df1 ==========================> \n{ret}')  # 원본에 적용하라고 했으므로 None 으로 나타남
print(f'retDF ==========================> \n{retDF}')


#### inplace 매개변수는 자주 나옴
# 보통 원본은 두고 복사본에 적용




# 열(column, 세로 데이터) 삭제 => drop(axis=1) 메서드 ===================================
# 행 방향 지정 => axis = 1 또는 axis = 'columns'
# sci 컬럼 삭제
colDF = df1.drop('sci', axis = 1)
print(f'colDF ==========================> \n{colDF}')  # 원본에 적용하라고 했으므로 None 으로 나타남
print(f'df1 ==========================> \n{df1}')


# 인덱스는 데이터가 존재해야만 쓰는 거라 iloc 가 아니라 loc 를 쓴다.


#================================================================================
# DataFrame & Series 다루기 => 추가
#================================================================================
# 행(rwo, 가로줄) 데이터 추가 ----------------------------------------------------
#변수명.loc['행이름/인덱스'] = 값
# 데이터 => 이름, 국어, 영어, 과학
df1.loc['의적'] = ['홍길동', 99,98,91]
print(f'df1 ==========================> \n{df1}')  # 원본에 적용하라고 했으므로 None 으로 나타남
print(f'df1.index ==========================> {df1.index}')


#행이름에 숫자 넣어도 가능
# 열 추가시 오류가 나타나는 경우
#df1.loc[10] = ['0'] # 컬럼의 수에 맞춰서 데이터를 주어야 에러가 안난다.


# 열(column, 세로줄) 데이터 추가 ----------------------------------------------------
#변수명['열이름/인덱스'] = 값

# 수학 과목 넣기
df1['math'] = [100,99,78,94]
print(f'df1 ==========================> \n{df1}')  # 원본에 적용하라고 했으므로 None 으로 나타남
print(f'df1.columns ==========================> {df1.columns}')


# 열 추가시 오류가 나타나는 경우
# df1['math2'] = [100] # 값을 갯수만큼 안주면 오류 뜸 
# print(f'df1 ==========================> \n{df1}')  # 원본에 적용하라고 했으므로 None 으로 나타남
# print(f'df1.columns ==========================> {df1.columns}')

# 받아온 데이터를 가지고 새로운 열, 행을 추가하여 원하는 데이터 추출
