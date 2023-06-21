# -----------------------------------------------------------------
# 인덱스(Index) 다루기
# -----------------------------------------------------------------
# 모듈/패키지 로딩 -------------------------------------------------
import pandas as pd

# DF 생성 ----------------------------------------------------------
df1=pd.DataFrame({'name':['마징가', '베트맨', '원더우먼'],
                    'kor': [87,97,69],
                    'eng': [99,73,89],
                    'sci': [71,95,62]})


# DF 데이터 확인하기
print(f'df1 ==========================> \n{df1}')
print(f'df1. index ==> \n{df1.index}')
print(f'df1. columns ==> \n{df1.columns}')


# [1] 특정 컬럼을 행 인덱스로 설정 =====================================
# DataFrame.set_index() 메서드 2개 이상일 경우, 리스트에 담는다. DataFrame.set_index([])
# 'name' 컬럼을 행 인덱스로 설정
nameDF2=df1.set_index('name')
print(f'df1==========================> \n{df1}')
print(f'nameDF2 =====================> \n{nameDF2}')


# 모든 행에 대한 값을 출력 => DF.loc[행인덱스]
for rIdx in nameDF2.index:
    print(rIdx, nameDF2.loc[rIdx], sep='\n', end='\n\n') #sep 행간 간격

print('-'*50)
sr1=nameDF2.loc['마징가']
print(type(sr1), sr1, sep='\n')


# [2] 인덱스 부분 변경 ================================================
# 전체 변경 => DF.index=[새로운 인덱스], DF.columns=[새로운 인덱스]
# DatatFrame.rename() 메서드 
# rename 일부 변경이 필요할 시 사용하면 편리함

# 행 인덱스 '마징가' '베트맨' '원더우먼' ==> '베트맨' ==> '홍길동'

print(f'rename ------------------------')

copyDF=df1.rename(columns={'베트맨':'홍길동'})
print(copyDF, end='\n\n')


# 행을 다 바꾸지 않고 내가 원하는 것만 바꾸는 것 가능
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df.rename(columns={"B": "bb"}, inplace = True))
print(df)

# 행(row) 인덱스를 변경 => 10,20,30 으로 변경

print(df.rename(index={0:10, 1:20, 2:30}, inplace=True))  #문자열이 아닌 정수로 나오게끔 설정해야함, 원본 데이터는 정수로 입력되었기 때문
print(df)

# 행(row) 인덱스를 변경 => 10,20,30 => '10', '20', '30' 로 변경

#print(df.rename(index={10:'10', 20:'20', 30:'30'})) 
df.rename(index=str, inplace=True) # 값이 변경되는 것이 아니므로 문자 형식으로 변경하면 됨
print(df.index)



# [3] 새로운 인덱스 지정 설정 =======================================
# 58페이지
# DataFrame.redindex([새로운 인덱스])
# 기존 인덱스랑 갯수나 이름 다를 수 있음
# => 기존 인덱스가 아닌 인덱스의 값은 존재 하지 않음 => NaN : Not a Number 약자

newDF=df.reindex(['10', '15', '20', '25'])
print('원본      DF => ', df, end= '\n\n')
print('변경된 인덱스 => ', newDF, end= '\n\n') # 해당하는 인덱스에 데이터가 비어있으면 NaN 로 표시, 공백이 아니다. 공백은 문자로 나타남


#ffill(forward fill) 은 앞에 값을 채워 넣는다는 것을 의미, bfill (big fill)
newDF=df.reindex(['10', '15', '20', '25'], method='ffill')
print('원본      DF => ', df, end= '\n\n')
print('변경된 인덱스 => ', newDF, end= '\n\n')


# NaN 값을 내가 원한는 값으로 채우기 => fill_valuse = 값
#newDF=df.reindex(['10', '15', '20', '25'], method='nothing')
#print('원본      DF => ', df, end= '\n\n')
#rint('변경된 인덱스 => ', newDF, end= '\n\n')



# [4] 판다스에서 지정하는 기본 인덱스로 초기화 설정 =======================================
# DataFrame.reset_index()([새로운 인덱스])
# 기존 인덱스 =======> 컬럼으로 추가된다. 

newDF2=newDF.reset_index()
print(newDF2)

newDF2=newDF.reset_index(drop=True)
print(newDF2)



