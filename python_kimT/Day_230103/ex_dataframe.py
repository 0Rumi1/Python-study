#-----------------------------------------------------------------------------
# 데이터 프레임(Data Frame)
# - 판다스의 구조화 데이터 타입
# - 구성 : 행과 열
# - 요소 : 행인덱스, 열이름
# ------------------------------------------------------------------------------------
# 패키지, 모듈 로딩 =================================
import pandas as pd

# DF 생성 실습 =--------------------------------------
# 데이터 => List 데이터 사용
data = [10, 20, 30], ['F','M', 'M'] #===> 2차원

df1 = pd.DataFrame(data)

# 데이터 확인 출력 
print(f'df1 => \n{df1}')

print(f'df1.index => {df1.index}')
print(f'df1.columns => {df1.columns}')
print(f'df1.shape => {df1.shape}')
print(f'df1.ndim => {df1.ndim}')
print(f'df1.dtypes => {df1.dtypes}')  #0번 타입은 object, 따라서, dtypes 은 object
print(f'df1.values => \n{df1.values}\n{type(df1.values)}')



#C 언어 시작 번호의 주소만 알면 배열이 되어 나타난다. 
# 배열의 장점, 빠르게 읽어낼 수 있으나 메모리 손실이 일어날 수 있음 => 크기가 정해져있을 경우, 배열을 사용하는 것이 처리속도가 훨씬 빠르다

# 데이터 => Duct 데이터 사용 (2)
data = {'name':['홍', '이', '박'], 'job':['학생', '학생', '주부']}  #coulum 은 name, job, range 는 정하지 않았으므로 자동으로 정수 0,1,2 가 나타남
df2=pd.DataFrame(data) 

# 데이터 확인 출력 
# 데이터 확인 출력 
print(f'df2 => \n{df2}')

print(f'df2.index   => {df2.index}')
print(f'df2.columns => {df2.columns}')
print(f'df2.shape   => {df2.shape}')
print(f'df2.ndim    => {df2.ndim}')
print(f'df2.dtypes  => {df2.dtypes}')
print(f'df2.values  => \n{df2.values}\n{type(df2.values)}') # 가로 한 줄씩 값이 나와야 제대로 뽑은 것


