#-----------------------------------------------------------------------------
# 파일 입출력 (I/O)
#-----------------------------------------------------------------------------
#모드 (mode)
#mode = 'w' : 파일이 존재하면 내용을 지우기, 그리고 쓰기
#             파일이 없으면 파일 생성하고 쓰기
#mode = 'a' : 파일이 존재하면 끝 부분에 내용 쓰기
#             파일이 없으면 파일 생성하고 쓰기
#-----------------------------------------------------------------------------

FILE_NAME='mydata.txt'

# 모드 'w' 로 파일 쓰기 

fp=open(FILE_NAME, mode='w', encoding='utf-8')
fp.write('000000')
fp.close()

# 모드 'z' 로 파일 쓰기 
# 존재하는 파일이면 오류발생
# 존재하지 않는 파일이면 파일생성 후 쓰기

FILE_NAME='happy.txt'
fp=open(FILE_NAME, mode='z', encoding='utf-8')
fp.write('Happy Happy')
fp.close()

print(f'allData type => {type(allData)}, {len(allData)}/n{allData}')



# 모드 'a' 로 파일 쓰기 
# 존재하는 파일 ====> 끝부분에 추가
# 존재하지 않는 파일 ====> 파일 생성 후 쓰기

fp=open(FILE_NAME, mode='a', encoding='utf-8')
fp.write('1 2 3 4 5 6 7')
fp.close()

print(f'readlines type => {type(readlines)}, {len(readlines)}/n{readlines}')


#readline() 파일 내용 1줄 가져오기

fp=open(FILE_NAME, mode='a', encoding='utf-8')
while True:
    line=fp.readline()
    print(f'[LINE] : {line}')
    if not line: break
fp.close()

print(f'line type => {type(line)}, {len(line)}/n{line}')