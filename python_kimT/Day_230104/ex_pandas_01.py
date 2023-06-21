#----------------------------------------------------------
# 연산 실습
#----------------------------------------------------------
# 모듈 로딩 -----------------------------------------------
import pandas as pd
FILE = r'Day_230103\dataFiles-20230103T063952Z-001\dataFiles\stock price.xlsx'

df = pd.read_excel(FILE)

# 데이터 확인 ==> info(), head(), tail(), describe()
df.info()
print(df.head(), df.tail(), sep='\n', end='\n\n') #head 는 맨 앞에 데이터 5개 추출, tail 맨 뒤에 데이터 5개 추출
print(df.describe(), end='\n\n')

# [1] 주식 ID, 주식명, 가격만 사용하도록 데이터 추출

#(1) value 컬럼을 삭제하거나

newdf = df.drop(['value'], axis=1)
print(newdf)

#(2) id, 주식명, 가격 데이터를 추출하기
selectdf = df[['id', 'value', 'price']]
print(selectdf.head(), selectdf.tail(), sep='\n', end='\n\n')

# [2] 가격에 대한 * 100 결과를 추가 ==> 컬럼추가
print(selectdf.price*100)
selectdf['price100'] = selectdf.price *100 #연산자
#df['price*100'] = df['price'].mul(100, fill_value= 0) #메서드를 이용해 직접 연산한 것
print(selectdf.head(), end='\n\n')


# 79 페이지 참고
# parse_dates 날짜 텍스트를 datetime64로 변환 여부 설정하기 > 데이터를 가져올 시 문자열의 날짜를 숫자로 변환하여 가져올 수 있음.
# 기본이 False 임, True/False 로 선택하여 지정함
# =====================================================================================================
# id 컬럼을 인덱스 설정 하라 ==> DataFrame.set_index(컬럼)
# 데이터 파일 읽어 들일 때 설정 ==> 매개변수(파라미터) 설정
print('='*50)
print(df.index, selectdf.index, sep='\n')


# 특정 컬럼 인덱스로 설정 ==> index_col 매개변수
# 로딩할 특정 컬럼 지정 ==> usecols = '' (원하는 컬럼만 지정해서 가져올 수 있다)

# skipfooter에는 숫자 타입의 값을 설정
# 지정한 값만큼 마지막 행 취득하지 않음
# 1을 지정 시 마지막 1행을 취득하지 않고, 2 지정 시 마지막 2행을 취득하지 않음
# stockDF = pd.read_excel(FILE, skipfooter=3) 


stockDF = pd.read_excel(FILE, skiprows=3, header=None) # 앞에 3개를 가져오지 않겠다는 뜻, 데이터가 삭제되었다는 뜻은 아님,  header 가 없다는 걸 넣어줘야함
#stockDF = pd.read_excel(FILE, usecols='B, D')

stockDF.info()
print(stockDF.index, stockDF.columns, sep='\n', end= '\n\n')
print(stockDF)


print('='*50)
from datetime import datetime # 날자시간관련 모듈

# parse_dates 매개변수 ==> 컬럼 지정 시 해당 컬럼의 타입이 datetime64로 변경
# dayfirst 매개변수 : False 기본값이 DD/MM 일/월 순서로 설정
# inter_datetimes_format 매개변수 : 날짜시간 포맷을 추정해서 파싱 (알아서 파싱해준다.)
# 내가 원하는 대로 날짜 형태를 바꾸고 싶으면 (파서를 지정해야함) 내가 직접 설정하여 파싱해야함  
# date_parser 매개변수 : 직접 날짜시간 포맷 설정 function
FILE2 = r'Day_230103\dataFiles-20230103T063952Z-001\dataFiles\banklist.csv'
_date_parser=lambda x : datetime.strptime(x, "%d-%b-%y")
bankDF = pd.read_csv(FILE2, parse_dates=['Updated Date'], date_parser=_date_parser)

#parse_dates=['Updated Date'], dayfirst=True, infer_datetime_format=True 다음에 perse_dates를 설정할때 뒤에 dayfirst 와 infer_datetime_format 도 함께 설정

#bankDF = pd.read_csv(FILE2, parse_dates=['Updated Date'], dayfirst=True, infer_datetime_format=True)
bankDF.info()
print(bankDF.head())
                    