
# 클래스 몸에 조금 익혀보기

# 다음은 간단한 함수들이다.

# def in_the_car(name):
#     print(f'{name}이가 차에 탑니다.')

# def fire(name):
#     print(f'{name}이가 라이터를 칙칙 킵니다.')

# def smoke(name):
#     print(f'{name}이가 담배를 쪽쪽 빱니다.')

# 위 세가지의 공통점을 찾아 클래스로 모아보겠다.

# class seokjun():
#     def __init__(self):
#         self.name = '석준'

#     def in_the_car(self):
#         print(f'{self.name}이가 차에 탑니다.')

#     def fire(self):
#         print(f'{self.name}이가 라이터를 칙칙 킵니다.')

#     def smoke(self):
#         print(f'{self.name}이가 담배를 쪽쪽 빱니다.')

# 석준의 행동들을 모아놓은 클래스 완성;

# 자 이제 석준을 하나 생성해서 담배를 펴보자

# man = seokjun()
# man.fire()
# man.smoke()


"""
챌린지

본인의 행동들을 함수로 먼저 구현한 후, 본인을 클래스로 정의하고 인스턴스를 생성 후 사용해보세요.
자유롭게 하시면 됩니다.
"""

# class Action:

#     def __init__(self):
#         self.name = '석준'

#     def action(self, play):
#         print(f'{self.name}이가 {play}를 합니다!')

#     def study(self, coding):
#         print(f'{self.name}이가 {coding} 공부를 하고 있습니다!')
    
#     def mycar(self, car):
#         print(f'{self.name}이가 {car}를 하고 있습니다!')

# myAction = Action()
# myAction.action('축구')
# myAction.study('Python')
# myAction.mycar('드라이브')
class Action:
    
    def __init__(self, name, doing = None, study = None, shower = None):
        self.name = name
        self.doing = doing
        self.__study = study
        self.__shower = shower

    def action(self):
        print(f'{self.name}가 {self.doing}를 하고 있습니다!')

    def study(self):
        print(f'{self.name}가 {self.__study}공부를 하고 있습니다!')

    def shower(self):
        print(f'{self.name}가 {self.__shower}을 하고 있습니다!')

myAction = Action('찬수', '헬스', '코딩', '목욕')

myAction.action()
myAction.study()
myAction.shower()
