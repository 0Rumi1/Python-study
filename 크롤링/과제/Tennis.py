
class Tennis_ball():
    def __init__(self, num, top, count):
        self.num = num
        self.top = top
        self.count = count
        self.result = 0
        top = -1
        ball = []
        
        # 인덱스를 사용하려고 top 을 사용하는 것 
        # Top = -1 > 1개가 들어오면 Top = 0 개가 되고 개수는 1개가 된다.
        # 이때, count 는 0 ==> 1개로 변함

    def menu(self, num):
        print('-'*30)
        print('1: 테니스 공 넣기\n2: 테니스 공 꺼내기\n3: 테니스 공 개수 출력\n4: 종료')
        print('-'*30)

        while True:
            try:
                push_ball = int(input('메뉴를 선택하세요: '))
                if push_ball > 4:
                    print('잘못된 메뉴 선택입니다.')
                elif push_ball == 1:
                    return self.pop

                elif push_ball == 2:
                    return self.push 
    
                elif push_ball ==3:
                    return self.ball_print

            except: print('잘못된 메뉴 선택입니다.')
            
            if push_ball == 4:
                return self.exit()
        

    def push(self, top, ball):
        for i in ball:
            ball += 1
            top += 1
            print('count: ', ball[0] )
            return self.ball_print
   
        if ball == 5:
            print ('공이 가득 찼습니다.')


    def pop(self, top, ball):
        if ball:
            ball -= 1
            top -= 1
            print('count: ', top )

            return self.ball_print
        if ball == 0:
            print('공을 모두 꺼냈습니다.')


    def ball_print(self, ball, top):
        
        #top 은 인덱스를 사용할 것
        print('[공의 개수]: ')
        self.result += num
        num += 1
        print('top: ', top)
        return self.result
        

    def exit(self):
        print('종료')


                




    