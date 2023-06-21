# ------------------------------------------------------------------------
# CSV FILE ==> DataFrame 객체로 저장
# - pandas.read_csv(경로파일명)
#-------------------------------------------------------------------------
import pandas as pd

# r 을 적으면 \역슬러시 무시됨
FILE = r'Day_230103\dataFiles-20230103T063952Z-001\dataFiles\banklist.csv'

# DF 객체 생성 ------------------------------------------------------------

bankDF = pd.read_csv(FILE)

print(f'bankDF ===> \n{bankDF}')

# DF 데이터 확인용 메서드 --------------------------------------------------
# [1] 전체 요약 정보 제공 메서드 => info()메서드
bankDF.info()


# [2] 앞부분 5줄(기본값) 실제데이터 보기 => head(n) 메서드
#     끝부분 5줄(기본값) 실제데이터 보기 => tail(n) 메서드

print(bankDF.head(), bankDF.tail(3), sep='\n')

#[3] 데이터의 기술통계를 적용한 결과 제공 => 데이터 분포 확인 ==> describe() 메서드
#    수치 데이터만 가능(기본값)
#    모든 데이터   가능(include ='all')
print(bankDF.describe(include = 'all'))




# 데이터 가지고 놀기 ===============================================
# 특정 컬럼만 뽑아보기
print(f'bandkDF.columns ==> {bankDF.columns}')



# (1) 4개 컬럼 =>'Bank Name', 'City', 'Closing Date', 'Updated Date'
newDF = bankDF[['Bank Name', 'City', 'Closing Date', 'Updated Date']]
print(newDF.info())
print(newDF.head(3))

# (2) 컬럼 중에서 인덱스로 설정 => set index([])
newDF.set_index(['Bank Name', 'City'], inplace = True)
print(newDF.info, newDF.columns, sep='\n', end='\n\n')
print(newDF.head(3))

# (3) 'Updated Date' 기준으로 가장 최근날짜부터 보여주세요.
# 가장 최근 날짜 => 내림차순 (ascending = False)
# object => str ----------> datetime 으로 바꾸어야함

# 문자열을 데이터값으로 바꾸기 위해, key 와 to_datetime 을 이용
newDF.sort_values(by=['Updated Date'], key=lambda col: pd.to_datetime(col), inplace=True)
print(newDF['Updated Date'].values)

