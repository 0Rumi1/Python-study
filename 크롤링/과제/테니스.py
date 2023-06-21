


#메뉴구성
# while문으로 반복하고
# 각 메뉴선택시 해당하는 함수로 실행하게끔
# 숫자이외에 값이 들어온 경우 try except

#1.공넣기 2. 공꺼내기 3. 공개수 4. 종료



prompt = '''

1.테니스 공 넣기
2.테니스 공 꺼내기
3.테니스 공 개수 출력
4.종료

메뉴를 선택하세요:
[공의 개수]: 
Enter number: '''


while number !=4:
    print(prompt)

try  :
    number = int(input('메뉴를 선택하세요: ')) # 4번 입력 시 프로그램 종료
                
except:
    print('잘못된 메뉴 선택입니다.')
                
        #숫자 예외처리 
                
                

                

                

    
    # def push(self):



    # def pop(self):



    # def num_print(self):

