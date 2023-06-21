# ---------------------------------------------------------------
# 객체지향언어 ----> 정보은닉(캡슐화)
# - 속성/필드    --> 비공개 private
# - 메서드       --> 비공개 private ==> 공개가능한 것만 공개 public
# ----------------------------------------------------------------

# BMI 지수 => 키와 몸무게로 계산
class A: 


    #속성 2개가지는 클래스-------------------------------------------
    #self는 클래스 안에서만 사용함
    def __init__(self, weight, height, bmi):
        self.__weight=weight #비공개 : 클래스 안에서는 어디든지 사용, 객체변수명으로 사용불가
        self.__height=height #비공개
        self.bmi=bmi         #공개 : 클래스, 객체변수명으로 사용가능   

    # 비공개 속성을 제어할 수 있는 메서드 -----------------------------------------------------
    # 비공개 속성의 값을 읽을 수 있는 메서드 => get속성명()
    # 비공개 속성의 값을 변경 할 수 있는 메서드 => set속성명()
    # get, set 을 처음에 설계할 때 만들지를 결정함, 그렇지만 웬만하면 다 만들어놓고 시작을 한다.

    def setWeight(self, weight):
        self.__weight=weight

    def getWeight(self):  #값을 가져온다 get 
        return self.__weight #return 보여줌

    
    #BMI 계산 해서 값 설정하는 메서드
    #BMI = weight/(height/100)*(height/100)
    def __calcBMI(self):
        self.bmi=self.__weight/((self.__height/100)*(self.__height/100))

    #정보제공 메서드
    def showInfo(self):
        self.__calcBMI()
        print(f'몸무게 : {self.__weight}')  # 또는 {self.getWeight()} 으로 쓸 수 있다.
        print(f'  키   : {self.__height}')
        print(f'  BMI  : {self.bmi}')

    ##사족) is 가 들어가면 True or False 가 값으로 나타난다는 말 

    #몸무게 증감 처리 메서드
    def diet(self, value):
        self.__weight= self.__weight+value #value 는 +4, -4 값으로 계산되므로 if 값을 하지 않아도 된다.



#인스턴스(즉 객체) 생성 ---------------------------------------------
#변수=클래스명()
me=A(160.3,78.3, '')

#인스턴스 속성 확인 ==> 변수명, 속성명
print('me.bmi => ', me.bmi)
print('me.__weight => ', me.getWeight())