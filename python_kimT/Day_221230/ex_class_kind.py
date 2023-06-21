# #----------------------------------------------------------------------------------
# # 사용자 정의 클래스 / 커스텀 클래스
# #----------------------------------------------------------------------------------
# # 만들고자 하는 프로젝트(프로그램)에서 사용할 데이터를 저장하는 타입
# #----------------------------------------------------------------------------------
# # 학생 정보를 저장하고 출력
# # => 학교, 이름, 학년 (속성만 담은 것을 구조체라 한다. => 클래스)

# #학생 1의 정보
# # 각 변수값을 지정
# school=''
# name=''
# grade=''

# #학생2 추가 
# #학생이 추가되면 또 변수값을 만들어야하는 번거로움과 반복을 하게 된다.
# school2=''
# name2=''
# grade2=''

# def study(subject):
#     print(f'{subject} 공부합니다')

# def test(subject):
#     print(f'{subject} 시험칩니다')

# def food(subject):
#     print(f'{food} 먹습니다')


# #따라서 리스트로 묶으면 관리도 쉽고, 또 적을 필요없이 편함
# #유지보수가 쉬움 (속성의 추가, 삭제 등 수정이 각 코드에 자동 적용이 된다)
# #=> 클래스 방법으로 아래 코드를 이름 하나로 묶어준다.

# school=[]
# name=[]
# grade=[]

# def study(subject):
#     print(f'{subject} 공부합니다')

# def test(subject):
#     print(f'{subject} 시험칩니다')

# def food(subject):
#     print(f'{food} 먹습니다')

#논외) self 는 새로운 공간이 만들어지는 것


# 클래스 스튜던트로 하나로 묶음 
class Student:
    #클래스 변수 - 모든 인스턴스 공유 (값을 바꾸지 않도록 하고 싶다면 튜플 사용)
    #           - 인스턴스 즉 객체 생성 없이 사용
    #           - 사용법 : 클래스명.클래스변수명
    school= "대구중학교" #서울 중학교도 포함해서 2개의 학교를 추가하고 싶다면? 안됨. 클래스는 객체 생성이 안되므로
    name= "홍길동"
    grade= 1
    rank=1 #정보를 추가 수정하기도 쉬워서 나머지는 자동으로 적용된다.

    #인스턴스 즉 객체 생성 및 초기화 메서드 => 생성자 메서드(Constructor Method)
    #새로운 메모리 공간에 생성 ===> self 담겨 있음
    def __init__(self, school, name, grade, schoolNum, num):  #객체 생성
        self.school=school
        self.name=name
        self.grade=grade
        self.schoolNum=schoolNum
        self.num=num

    def aa(self): #(함수)
        pass

    def play(self): #우리가 self 넣은게 아니라 시스템이 self를 넣는 것 
        print(self.name) # => self 메모리의 네임을 불러옴 
        print(Student.school) #=> 클래스를 부르고 싶다면 무조건 클래스명 넣고 불러야함
        self.aa() #self 를 가지고 있는 것들은 self를 기준으로
        Student.study() #=> study는 Student 클래스의 소속


    #클래스 메서드 - 인스턴스 즉 객체 생성 없이 사용
    #             - 사용법 : 클래스명.클래스메서드명
    def study(subject):
        print(Student.school) #클래스 안의 스쿨이므로, print(school) 은 불러오지 못함, print(Student.school) 로 찾아달라고 지정해야함
        print(f'{subject} 공부합니다')

    def test(subject):
        print(f'{subject} 시험칩니다')

    # def food(subject):
    #     print(f'{food} 먹습니다')

        


#==> 클래스 속성 및 메서드 사용
st1=Student()
print(f'st1.school : ', st1.school)
st1.study('미술')

print(f'Student.school: ', Student.school)
Student.school='제주고등학교'
Student.study('국어')


# st1=Student('대구중학교, 홍길동', 1,1,10)
# st1.play()
# #st1.test("국어")
# Student.test("Happy")

# #클래스용 메서드와 인스턴스 메서드를 구분해서 사용해야한다

def eat(food):
    print(f'{food} 먹습니다 ')
    return 7

Student.study('공부')
st1=Student(1,1,1,1,1)
st1.eat() #=> 하나뿐이라 eat의 주소값이 나와서 실행됨
#만약 eat() 함수안에 ('찜닭') 을 넣는다면 오2개를 호출하는 것으로 받아들여 오류 발생