#--------------------------------------------------------------------------------
# 파일 입력과 출력 (I/O)
# 스트림(Stream) : 흐름, 데이터의 흐름
#                - 종료  -입려 스트림, 출력 스트림
#--------------------------------------------------------------------------------
# with ~ as
# close기능을 자동 실행
#--------------------------------------------------------------------------------
FILE_NAME = 'new_year.txt'

#파일 쓰기(write)
# mode - w :덮어주기
#      - a :추가
#      - x :이미 존재하는 파일이면 오류 발생, 존재하지 않는 파일만 가능
#--------------------------------------------------------------------------------
with open(FILE_NAME, mode='w', encoding='utf-8') as f: #open() 를 f 라고 하겠다(as)
     f.write("새해 복 많이 받으세요. 2023 검은 토끼")


#파일 읽기(read)
#mode - r : 일기
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
with open(FILE_NAME, mode='r', encoding='utf-8') as f:
    print(f.read())


#파일 복사(Copy)
# 조건 : 파일명 끝 부분에 숫자 추가
# 예시 : data.txt => data_1.txt, data_2.txt, ...
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#My code
FILE_NAME = 'data.txt'
num = 1

def copyFile(file, copy):

    with open(FILE_NAME[num], mode='r', encoding='utf-8') as f:
        print(f.read())

        if FILE_NAME == FILE_NAME:
            
            
#----------------------------------------------------------------------------------

def copyFile(filename):

    #파일명 만들기
    _filename = filename.replace('txt', '_1.txt') 
    print(f'_filename : {filename}')

    #파일 읽어서 새 파일에 쓰기
    #방법(1)
    with open(filename, mode='r', encdoing='utf-8') as f:
        data = f.read()
    
    with open(_filename, mode='w', encdoing='utf-8') as f:
        f.write(data)

    #방법(2)
    #with open(_filename, mode='r', encdoing='utf-8') as f1:
        #with open(_filename, mode='w', encdoing='utf-8') as f2:
            #f2.write(f1.read())

copyFile(FILE_NAME)



#라인에 번호 추가하기
#----------------------------------------------------------------------------------


def copyFile(filename):
    #파일명 만들기
    _filename = filename.replace('txt', '_1.txt') 
    print(f'_filename : {filename}')

    #파일 읽어서 새 파일에 쓰기
    with open(_filename, mode='r', encdoing='utf-8') as f1:
        with open(_filename, mode='w', encdoing='utf-8') as f2:
            f2.write(f1.read())

#----------------------------------------------------------------------------------

def copyFile(filename):
    #파일명 만들기
    _filename = filename.replace('txt', '_1.txt') 
    print(f'_filename : {filename}')

    #파일 읽어서 새 파일에 쓰기
    with open(_filename, mode='r', encdoing='utf-8') as f1:
        with open(_filename, mode='w', encdoing='utf-8') as f2:
            #라인에 번호 추가

            lines=f1.readlines()
            for idx in range(1, len(lines)):
                f2.write(f'[{idx}]'+lines[idx-1])
            
copyFile(FILE_NAME)