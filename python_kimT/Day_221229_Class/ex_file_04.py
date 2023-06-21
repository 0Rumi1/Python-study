#파일 읽기 살펴보기

FILE_NAME='happy.txt'

fp=open(FILE_NAME, mode='r', encoding='utf-8')
allData=fp.read()
fp.close()

print(f'allData type => {type(allData)}＼n{allData}')

