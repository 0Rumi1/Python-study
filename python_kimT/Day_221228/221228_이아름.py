#구구단 문제 풀이
#end='/n' if n==5 #줄바꿈으로 주고, IF 문으로 열 조정하기
#for dan in range(2,9)
#    for n(1,10)

#for num in range(1,10): #단이 아니라 숫자가 고정, dan > num range를 (1,10)
#    print(f'---{dan}단---', end=' ')  #end='' 공백 주면 횡으로 정렬
#    for dan in range(2,10):#dan*num:0>2 자릿수가 두칸, 2칸이 안되면 공백, 기본으로 오른쪽 정렬
#        print(f'{dan}*{num}={dan*num:0>2}', end = 'n' if dan==9 else '0')



#[2]
#def addData(*nums):
#    total=0
#    for num in nums:
#        total+=num
    
#1    return total if len(nums)>0 else None #입력 받은게 0보다 크면 그대로 표시, 값이 없으면 NONE 이 나오도록 설정
#2    if len(nums)>0:
 #       return total #0보다 작으면 return 값은 자동으로 None 값이 나온다. 

#print (addData())
#print (addData(True, False, False))


#[3] #index 뽑거나, key 값을 출력의 이름으로 설정, 과목 점수 값) #dic (dic) 넣거나


#[4]
#starIdx = month if starDates[month]<=day else month-1 #날짜가 작거나 같으면 월 그대로 > 별자리와 띠 출력


#hex(ord(n)) #16진수 hex, ord 숫자 > 문자
#bin(ord(A)) #2진수 bin, ord 문자 > 숫자

print("ord(A): ", ord('가'))
print("hex(ord(A)): ", hex(ord('가'))) #hex(ord(n)) #16진수 hex, ord 숫자 > 문자
print("bin(ord(A)): ", bin(ord('가'))) #bin(ord(A)) #2진수 bin, ord 문자 > 숫자


[14]
#num=1234
#num//1000
#num/%1000