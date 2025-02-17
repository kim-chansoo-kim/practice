# 기초문법 숙달, 딕셔너리 편
# 딕셔너리란 ?
# { key : value } 형태로 저장되는 데이터 구조 입니다.

# 접근 방법

# dict[key] 로 접근하면 value 를 리턴합니다.
# value
# 필수 메서드 : keys() , values()

dict = { '최보정' : 1995 , '이형우' : 1996 , '강석준' : 1995 , '우동관' : 2000 , '황석준' : 1996 , '김찬수' : 2000 }

# 접근 방법
print(dict['최보정']) # 1995

# keys() : 딕셔너리의 모든 key값을 반환한다.
print(dict.keys()) # dict_keys(['최보정', '이형우', '강석준', '우동관', '황석준', '김찬수'])

# values() : 딕셔너리의 모든 value값을 반환한다.
print(dict.values()) # dict_values([1995, 1996, 1995, 2000, 1996, 2000])

# 사용 꿀팁, values 혹은 keys 를 리스트 등에 담아 저장가능합니다.
temp = dict.values()
print(temp) # [1995,1996,1995,2000,1996,2000]

# 챌린지 .
""" 
강황석준 조 멤버들의 나이를 구하는 로직을 작성 후, 출력해보세요. 
조건 . 
여기서 말하는 나이는 (현재년도 - 출생년도) 입니다.
계산은 컴퓨터가 해야합니다, 손수 계산해서 출력하지 마세요.
정답을 구하는 방법은 겁나 많습니다. 결과값이 정확하게 나오게만 해주세요.

이번 문제는 다 같이 모여서 한 분씩 코드리뷰 하겠습니다.

<결과값> `
최보정 : 30세
이형우 : 29세
강석준 : 30세
우동관 : 25세
황석준 : 29세
김찬수 : 25세
"""
for keys ,values in dict.items():
    print(f'{keys} : {2025 - values}세\n', end='')

# 여기 아래 코드 작성 !