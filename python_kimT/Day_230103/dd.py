
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

import pandas as pd
bankFILE = r'Day_230103\dataFiles-20230103T063952Z-001\dataFiles\banklist.csv'
bf = pd.read_csv(bankFILE)


bf2=bf.set_index('Bank Name', 'City', 'Closing Date', 'Updated Date')
print(f'bf==========================> \n{bf}')
print(f'bf2==========================> \n{bf2}')



desDF=bf.sort_index(axis=1, ascending=False)
print(desDF.index, desDF, end='\n\n')