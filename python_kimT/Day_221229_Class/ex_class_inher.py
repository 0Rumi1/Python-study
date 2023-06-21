# 상속(Inhertance) - 기존 클래스(=부모 클래스) 재사용 및 기능 확장 

# 포인트를 나타내는 데이터 타입 => 클래스
# - 클래스명
#   Point2D
# - 속성/필드
#   좌표 x, y
# - 기능/역할
#   점 찍기
#   동그라미 그리기
#   별 그리기


#---------------------------------------------------------------------


# class Point2D:

#     def __init__(self, x, y):
#         self.x=x
#         self.y=y

#     def pointing(self):
#         print(f'{self.x}, {self.y}에 점찍기')

#     def drawcolor(self, color):
#         print(f'{self.x}, {self.y}에 {color} 색상 칠하기')

# redPoint=Point2D(2, 3)
# redPoint.drawcolor("레드")



class Point2D: #클래스명 지정시 숫자가 먼저 시작되면 안됨
    #클래스 변수

    #인스턴스 생성 및 변수 초기화 메서드
    def __init__(self, x, y):
        self.x=x
        self.y=y

    #인스턴스 메서드
    def pointing(self):
        print(f'({self.x}, {self.y})에 점찍기')

    def drawCircle(self, color):
        print(f'({self.x}, {self.y})위치에 {color} 색상 동그라미 그리기')

    def drawAction(self, action):
        print(f'({self.x}, {self.y})위치에 {action} 별 그리기')  

    def drawdouble(self, color, action):
        print(f'({self.x}, {self.y})위치에 {action} {color} 별 그리기')


bluePoint=Point2D(20, 4)
bluePoint.drawCircle("파랑색")
bluePoint.drawAction("반짝반짝")




# #--------------------------------------------------------------------- 

# # 3D 입체공간에 포인트를 나타내는 데이터 타입 => 클래스
# # - 클래스명
# #   Point3D
# # - 속성/필드
# #   좌표 x, y, z
# # - 기능/역할
# #   점 찍기
# #   동그라미 그리기
# #   별 그리기


# # class Poin3D: #클래스명 지정시 숫자가 먼저 시작되면 안됨
#     #클래스 변수

#     # #인스턴스 생성 및 변수 초기화 메서드
#     # def __init__(self, x, y, z):
#     #     self.x=x
#     #     self.y=y
#     #     self.z=z

#     # #인스턴스 메서드
#     # def pointting(self):
#     #     print(f'({self.x}, {self.y}, {self.z})에 점찍기')

#     # def drawCircle(self, color):
#     #     print(f'({self.x}, {self.y}, {self.z})위치에 {color} 색상 동그라미 그리기')

#     # def drawCircle(self, action):
#     #     print(f'({self.x}, {self.y}, {self.z})위치에 {action} 색상 별 그리기')    





# #----------------------------------------------------------------------------------------
# #[Point2D 클래스 상속 받음]
# #부모클래스/슈퍼(super) 클래스 -- Point2D
# #자식클래스/서브(sub) 클래스 -- Point3D
# #상속 관계 사용되는 키워드 => super
# #----------------------------------------------------------------------------------------

# class Point3D(Point2D):

#     #인스턴스(즉 객체) 생성 및 속성 초기화 메서드 
#     def __init__(self, x, y,z):  #__init__ 을 자동완성 시, 부모클래스의 def 자동 완성됨
#         super().__init__(x, y)
#         self.z=z

#     #부모 클래스로부터 상속 받은 메서드의 구현 부분을 변경 => 오버라이딩(overriding)
#     #동일 - 메스드명, 매개변수
#     #변경 - 기능 구현 코드
#     def drawCircle(self, color):
#         print(f'({self.x}, {self.y}, {self.z}위치에 {color} 색상 동그라미 그리기')
                                                 

# #인스턴스 (즉 객체) 생성하기 ==> 클래스명(매개변수) <- __init__ 메서드랑 갯수 같아야 함
# bluePoint=Point2D(20, 4)
# bluePoint.drawCircle("파랑색")
# bluePoint.drawSatr("반짝반짝")

# pinkPoin=Point3D(10,5,3)
# pinkPoin.drawCircle("pink")
