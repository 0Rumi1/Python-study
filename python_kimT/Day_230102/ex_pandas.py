import pandas as pd

# 시리즈(Series) 데이터 ====================================================
# pandas.Series(데이터)
# 속성(Attribute) : index, values, ndim, shape, ...
#==========================================================================
# Series 객체 속성 출력 함수
# printSeries
def printSeries(srObj, srObjName):
    print(f'{srObjName} \n{srObj}')
    print('--------------- ')
    print(srObj.index)
    print(srObj.values)
    print(srObj.ndim)
    print(srObj.shape)

#__name__ : 매직 변수, 파이썬 시스템에서 값을 설정
# 해당 파이썬 파일이 실행 중 여부 확인
# 실행 중 ==> __main__
# import될 경우 ==> 파일명

print(f'__name__ =>{__name__} ')
if __name__ == 'main':
 # import 를 여기에 넣어도 무방


# (1) 데이터 => 리스트 데이터  srObj

sr = pd.Series([10,20,30]) #출력값 0,1,2 는 시리즈에서 자동으로 부여
printSeries(sr, 'sr')

#시리즈 객체의 속성 확인 => 변수명.속성명
# print(sr.index)
# print(sr.values)
# print(sr.ndim) #몇 차원인지, 1차원이므로 1로 출력
# print(sr.shape) #튜플 3개

# (2) 데이터 => 딕셔너리 형태 데이터
sr2=pd.Series({'name':'Hong', 'age':12, 'loc': 'Deagu' })
print(sr2, 'sr2')

# print(f'sr2====>\n(sr2)')
# print('--------------- ')
# print(sr2.index)
# print(sr2.values)
# print(sr2.ndim)
# print(sr2.shape)

# (3) 데이터 => 튜플 형태 데이터
sr3 = pd.Series((11, 22))
printSeries(sr3, 'sr3')

# print(f'sr3====>\n(sr2)')
# print('--------------- ')
# print(sr3.index)
# print(sr3.values)
# print(sr3.ndim)
# print(sr3.shape)



