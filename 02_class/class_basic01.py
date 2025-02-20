

# 클래스란 ?

# 어떤 객체의 특성,특징 등등등을 모아둔 '틀' 으로서 인스턴스를 찍어낼 수 있다.


# 기초문법

class people():

    # 클래스가 가지고 있는 명사 , 멤버 변수 선언 예시
    # 멤버 변수
    # private : 클래스 내에서만 접근이 가능한 변수. 변수 이름 앞에 __을 붙혀주면 된다.
    # public : 클래스 밖에서도, people.name 등으로 접근이 가능하다.

    # __init__ (생성자) : 클래스의 인스턴스가 생성될 때 자동으로 실행되는 함수이다.

    def __init__(self,name): # 매개변수 설정, 내가 input을 받아서 사용하고싶은 변수가 있다면, 매개변수를 self 이외에 설정을 해주어야한다. 여기서는 name을 선언하여 사용했다.
        print('생성자가 실행되었습니다!')
        self.__name = name
        self.__hand = 3
        self.foot = 5
        self.eyes = '눈'
        self.body = '몸'
        self.face = '얼굴'

    def __str__(self):
        return f'ㅗㅗ'
    

    # 클래스가 할 수 있는 행동(동사), 멤버 함수(메서드) 선언 예시
    def shake(self,object): # 매개변수 설정, 이 또한 아무것도 받지 않으려면 self만 설정해놓으면 된다.
        self.new = '새로운 멤버 변수'
        return f'{self.name}이가 {object}를 흔듭니다 !'
    
    def po(self):
        self.hand + self.foot
    
    

# 클래스 사용하기

# people 클래스의 인스턴스 생성 후 human 이라는 변수에 담았다 !
human = people('최보정') # 생성자가 실행되었습니다!

print(human)
"""
- 연습 -
자신의 이름을 가진 people 인스턴스를 생성한 후 손을 흔들어보세요.

출력 결과 
생성자가 실행되었습니다!
본인의 이름이가 손을 흔듭니다 !

아래에 코드 입력
"""
class people():
    def __init__(self, name):
        self.name = name
        print('생성자가 실행되었습니다!')

    def __str__(self):
        return f'human : {self.name}'
        
    def shake(self):
        print(f'{self.name}가 손을 흔듭니다!')


human = people('김찬수')

human.shake()