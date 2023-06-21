#----------------------------------------------------------------------------------------
#파일 읽기쓰기 => 입출력(1/0)

#(1)열기 open   => 동작모드 mode='w' 쓰기 write mode = 'r' 읽기 read
#(2)쓰기 & 읽기
#(3)닫기 close
#----------------------------------------------------------------------------------------

#[[파일 쓰기]]
FILE_NAME = 'data.txt', 'ex_class_03.py'


# (1) 파일 열기 open(파일경로+파일명, 모드, 인코딩)
fp=open(FILE_NAME[0], mode='w', encoding='utf-8')

# (2) 쓰기 => write(*데이터*)
fp.write("Good＼n")
fp.write(" Happy")


# (3) 닫기 => close()
fp.close()

#[[파일 읽기]]
#(1) 파일 열기( 파일경로+파일명, 모드, 인코딩)


fp=open('Day_221229_Class\ex_class_03.py', mode='r', encoding='utf-8')

# (2) 파일 읽기 => read() : 파일 안에 모든 내용 가져오기 ==> str 타입
allContext=fp.read()

# (3) 파일 닫기 
fp.close()

# 파일 내용 확인
print(f'allContext => {allContext}')