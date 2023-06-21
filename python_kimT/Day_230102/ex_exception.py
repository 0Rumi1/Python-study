# ----------------------------------------------------------------------------
# 예외처리(Exception Handling)
# 실행 중 발생되는 오류로 프로그램이 중단되는 것을
# 막아주기 위한 방법
# ----------------------------------------------------------------------------

num = 10

try:
    num2 = int(input("숫자 입력: "))
    print(f'{num/num2} = {num/num2}')

except Exception as e: # Exception 은 모든 에러 발생 시 모두 받아들인다.
    print(f'Error : {e}')


# 각 오류 발생 시 각각의 오류마다 이름을 주거나, 특별한 처리를 하고 싶다면 아래 코드를 이용하면 된다.
except ZeroDivisionError as e:   #0 오류가 아닐 시 다음 오류 상황으로 넘김
    print("ERROR :", e)
    print(f'{e}')
    #pass              # 오류를 무시한다는 뜻

except ValueError as ve: # 엔터 오류 상황에서 아래 내용 출력 
    print("ERROR :", ve)


num = 10
try:
    num2 = int(input("숫자 입력: "))
    print(f'{num/num2} = {num/num2}')

except Exception as e: # Exception 은 모든 에러 발생 시 모두 받아들인다.
    print(f'Error : {e}')
finally:
    print(f'항상 실행') # Finally 오류가 생기든 안생기든 항상 실행된다, 예외와 상관없이 항상 실행하고 싶은 내용이 있다면 finally 사용
    # 예를 들면, 파일을 열어 코드를 실행 했을 시, 오류 발생 여부와 관계없이 파일을 닫아야한다. => 이때, finally 아래 file.close() 를 넣어준다.



FILE = 'rrr.txt'
try:
    fp = open(FILE, mode = 'w')
    fp.write(12345) #=> 정수를 넣어 오류 발생 시킴
    
#except 는 순차적으로 에러 체크
except FileExistsError as e: # Exception 은 모든 에러 발생 시 모두 받아들인다.
    print(f'이미 존재하는 파일이다')
except FileNotFoundError as e: # Exception 은 모든 에러 발생 시 모두 받아들인다.
    print(f'존재하지 않는 파일이다')
except Exception as e: # Exception 은 모든 에러 발생 시 모두 받아들인다.
    print(f'Error')
finally:
    if fp:
        fp.close()  #except 안에 if 를 넣어도 된다.
        print("파일 닫기")
    
    else:
        fp.close()
        print("파일 없음")

