#--------------------------------------------------------
# 정렬(Sort) 다루기
# - 인덱스 기준 정렬 => 오름차순 (작은 숫자 >> 큰 숫자), 내림차순(큰 숫자 >> 작은 숫자)
# - 데이터 기준 정렬 => 오름차순 (작은 숫자 >> 큰 숫자), 내림차순(큰 숫자 >> 작은 숫자)

# 모듈/패키지 로딩
import pandas as pd

#DF 생성
df1 = pd.DataFrame({'name': ['마징가', '베트맨', '원더우먼'],
                    'kor': [85,34,67],
                    'eng':[65,22,98],
                    'sci':[72,99,31]})

print(df1)

# [1] 인덱스 기준 정렬 => 내림차순
# 행기준, 내림차순

desDF=df1.sort_index(ascending=False)
print(desDF.index, desDF, sep='\n', end='\n\n')


#열기준, 내림차순
colDesDF=df1.sort_index(axis=1, ascending=False)
print(colDesDF.index, colDesDF, sep='\n', end='\n\n')

#열기준, 오름차순 (True 값으로)
colDesDF=df1.sort_index(axis=1, ascending=True)
print(colDesDF.index, colDesDF, sep='\n', end='\n\n')


# [2] 데이터(즉 값) 기준 정렬 => 내림차순
# DataFrame.sort_values()
#Series.str.upper 와 같이 str 메서드 쓸 수 있음
df2=df1.sort_values(by=['name'], ascending=False)
print(df2, end='\n\n')

df2=df1.sort_values(by=['kor', 'eng'], ascending=False)
print(df2, end='\n\n')



# 특정 컬럼에 값 넣기
print('-'*50)
print(df2['name'], df2.name, sep='\n')

df2.name = ['B-Man', 'mazinga', 'Woman']
print(df2['name'], df2.name, type(df2.name),sep='\n') #=> 타입 시리즈


print(df2.name[1], type(df2.name[1]), df2.name[1].lower())
#ignore 인덱스는 기존의 인덱스는 무시하겠다는 뜻


