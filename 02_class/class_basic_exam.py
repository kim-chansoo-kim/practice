
# 챌린지 !! 내 생각을 클래스화 해보기

# 아래의 문구를 정리해서 클래스로 만들어 보세요.

"""
찬수는 문자열을 공부하다 빡쳐서, 문자열 컷팅기 cut_string 클래스를 만들기로 마음 먹었습니다.
문자열 컷팅기, 즉 cut_string 클래스는 이러한 방식으로 동작합니다.

멤버변수로는 self.string
멤버함수로는 self.cutting
하나씩 구현하려고 생각한 찬수 입니다.

1. 인스턴스 생성시
- cut = cut_string('문자열') :  터미널 화면에 "분노의 문자열 컷팅기 생성!" 이 출력됩니다. 
                                문자열을 입력 받아야만 생성됩니다. 그리고 self.string 멤버변수안에 문자열 이 입력됩니다.
2. 멤버함수 호출시
- cut.cutting(n) : n은 정수입니다. n을 입력받아 self.string 의 인덱스 n 을 기준으로 두개의 문자열을 생성합니다. 문자열은 리스트에 담겨 "반환" 됩니다.
                    규칙 : 잘린 문자열은 예시와 같이 저장됩니다.
                    ex) self.cutting = 'python' , n = 3 ---> 결과 : result = [pyt,hon]
"""



class cut_string:
    def __init__(self,string):
        print("분노의 문자열 컷팅기 생성!")
        self.string = string

    def cuttings(self,n):
        return [self.string[:n],self.string[n:]]


cut = cut_string('python')
print(cut.cuttings(3))



class cut_string:
    def __init__(self,string):
        print("분노의 문자열 컷팅기 생성!")
        self.string = string

    def cutting(self,n):
        return [self.string[:n],self.string[n:]]

# 위에 클래스를 생성해서 , 아래 코드의 에러 메세지를 없애주세요 ~
cut = cut_string('강황석준')
print(cut.cutting(1))
# 출력 ['강','황석준']