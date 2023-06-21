#상속
#큰 개념을 부모로, 사람은 선생님인가? X
#선생님(자식)은 사람(부모)인가? o
#상속을 활요할 때 공통된 것만 뽑기

class Person:

    def __init__(self, school, cr, name, age):
        self.school=school
        self.cr=cr
        self.name=name
        self.age=age

    def printInfo(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'학교 : {self.school}')        
        print(f' 반  : {self.cr}')


#선생님을 나타내는 데이터 타입 => 클래스 
# - 속성/필드
# 수업, 칠판, 회초리, 과목, 숙제, 채점
#---------------------------------------
# 이름, 성별, 나이, 과목, 클래스, 학교
# - 메서드 (기능)
# 가르치다 숙제를 내다  (점수를) 매기다 


class T:
    def __init__(self, work):
        self.work=work
        

    def teaching(self, subject):
        print(f' {self.work}를 내다')
        print(f'{subject} 과목의 {self.work}를 내다')

kim=T('숙제')
kim.teaching("python")


#----------------------------------------------------------

class Teacher:
    
    def __init__(self, name, sex, age, subject, cr, school):
        self.name=name
        self.sex=sex
        self.age=age
        self.subject=subject
        self.cr=cr
        self.school=school
    
    def teaching(self):
        print(f'{self.name}선생님이 {self.cr}반에서 {self.subject}과목을 가르친다')

 #------------------------------------------------------------------------
    
class Teacher(Person):

    def __init__(self, school, cr, name, age, sex, subject):
        super().__init__(school, cr, name, age, sex, subject)

        self.name=name
        self.sex=sex
        self.age=age
        self.subject=subject
        self.cr=cr
        self.school=school
    
    def teaching(self):
        print(f'{self.name}선생님이 {self.cr}반에서 {self.subject}과목을 가르친다')

#-------------------------------------------------


#상속

#학생을 나타내는 데이터 타입 => 클래스 
# - 속성/필드
# 교복, 야자, 수업, 시험, 등수
#------------------------------------------
# 학교, 학년, 반, 이름, 나이
# - 메서드 (기능)
# 공부하다 시험을 치다


class Student:

    def __init__(self, school, grade, cr, name):
        self.school=school
        self.grade=grade
        self.cr=cr
        self.name=name

        
        def study(self, subject):
            print(f'{self.name}가 {subject}과목을 공부한다')

#----------------------------------------------------------------

class Student(Person):

    def __init__(self, school, grade, cr, name, age):
        super().__init__(school, cr, name, age, grade)
        self.school=school
        self.grade=grade
        self.cr=cr
        self.name=name

        
        def study(self, subject):
            print(f'{self.name}가 {subject}과목을 공부한다')


    
#---------------------------------------------------------------------
#매개변수 => 값, 가변값, 키=값 가변, 디폴트값
#---------------------------------------------------------------------

def calc(num1, num2, op='+'): #디폴트값은 항상 뒤로 넣어두는게 편이 (op='+')
    #op2 는 여러개를 넣었을 때 어떻게 나올지를 보여주는 예시일 뿐 
    if op =='+':
        return num1+num2
    elif op =='-':
        return num1-num2
    elif op == '*':
        return num1*num2
    elif op =='/':
        return num1/num2 if num2>0 else '0으로 나눌 수 있습니다'

print(calc(10, 2, '*'))
print(calc(10, 2))

#=====================================================================

def calc(num1, num2, op='+'):
    
    if op =='+':
        return num1+num2
    if op =='-':
        return num1-num2  #if 문을 하고 따로 검사할 것이 없으면 elif 를 쓰는 것이 더이상 체킹하지 않고 결과를 도출한다.
    if op == '*':
        return num1*num2
    if op =='/':
        return num1/num2 if num2>0 else '0으로 나눌 수 있습니다'

print(calc(10, 2, '*' ))
print(calc(10, 2))