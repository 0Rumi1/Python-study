#연락처 프로그램을 구현하고자 합니다.
#-----------------------------------------
# - 기  능 => 연락처 저장 / 삭제 / 수정
# - 데이터 => 이름, 전화번호, 사진, 별명, 직장, 그룹, 이메일...
#-----------------------------------------
#(1) 연락처에 사용될 클래스를 생성하세요.
#
#-----------------------------------------

class contact:

    def __init__(self):
        self.member=Member() #여러명은 list, 튜플, dic, set/ self 한명

#딕셔너리로 하는 경우, 전화번호를 KEY값으로 두고, 데이터 값마다 추가

#case 없이
contact={}
contact['010'] = {'name': 'hong', 'email': 'hong@naver.com'}
contact['017'] = {'name': 'hong'}
contact['018'] = {'email': 'hong@naver.com'}
contact['019'] = {}



def saveContact(phone, *info):
    #존재 여부 체크, 이미 있는지 확인을 위함(멤버 연산자 in)
    if phone not in contact: 
        contact[phone]=phone
    else:
        print('이미 저장된 전화번호입니다.')

#-----------------------------------------
# 연락처 프로그램 데이터 클래스 => 데이터 타입
# - Member
# - 필수 데이터 => 이름, 전화번호, 이메일
# - 선택 데이터 => 별명, 사진, 주소, 생일
#-----------------------------------------

#class Member:
    #클래스 변수

    #인스턴스 변수 생성 및 초기화 메서드

class Phone:

    def __init__(self, maker, number, color):
        pass
        self.phone = phone
        self.name = name 

    #번호를 저장하고 나머지 데이터 값은 선택 사항으로 하고 싶다면 디폴트로 둔다. (alias='') 와 같이

    def __init__(self, phone, name, alias='', picture='', email='', addr='', birth=''):
         self.phone = phone
         self.name = name 
         self.alias= alias
         self.picture=picture
         self.email=email
         self.addr=addr
         self.birth=birth

    #인스턴스 메서드를 사용해서 한꺼번에 호출
    def showInfo(self):
        print(f'--- [{self.phone}]---')
        print(f'이름 [{self.name}]')
        print(f'주소 [{self.addr}]')
        print(f'별명 [{self.alias}]')
        print(f'생일 [{self.birth}]')


mem=Member('010-111-1212', 'hong')
mem2=Member('010-111-1212', 'hong', addr='대구시')
mem.showInfo()
mem2.showInof()


#은행 관리 프로그램을 구현하고자 합니다.
#-----------------------------------------
# - 기  능 => 계좌 개설, 해지, 입금, 출금
# - 데이터 => 계좌번호(가장 중요한 정보라 볼 수 있다), 예금주, 개설 날짜, 이율, 잔액, 개설지점 >> 모든 정보를 하나로 묶는 class 만들면 됨
#-----------------------------------------
#(1) 연락처에 사용될 클래스를 생성하세요.
#-----------------------------------------
#-------------------------------------------

#은행 관리 프로그램 데이터 클래스 => 데이터 타입
#-----------------------------------------
# - Account
# - 필수 데이터 => 계좌번호, 예금주, 개설 날짜, 이율, 잔액, 개설지점, 주민등록번호
# - 선택 데이터 => 없음
# - 비공개 데이터 => 주민등록번호 (안보여줘도 되는 정보)
#-----------------------------------------
#-----------------------------------------
class Account:
    #클래스 변수
    BANK_NAME = 'DGB'

    #인스턴스 변수 생성 및 초기화
    def __init__(self, number, name, date, rate, balance, branch, jumin):
        self.number=number
        self.name=name
        self.date=date
        self.rate=rate
        self.__balance=balance
        self.__jumin=jumin  #비공개, __ 추가 => 클래스 밖에서 사용 불가 

    # 인스턴스 메서드 (클래스 안에서 하는 작업)
    def accountInfo(self):
        print(f'---[{self.name}]---')
        print(f'예 금 주 : {self.name}')
        print(f'주민번호: {self.__jumin}') #사용 가능
        print(f'개설 날짜: {self.date}')
        print(f'이율: {self.rate}')
        print(f'잔액: {self.__balance}')


myAccount=Account('111', 'm', '121', '0.1', 1000, '-', '010101')  #클래스 밖임
myAccount.accountInfo()
print('공개데이터 ', myAccount.rate)
print('비공개데이터 ', myAccount.__balance)
