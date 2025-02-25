import bingo
import aimlap

while True:
    print('강황석준 조의 미니게임 천국에 오신걸 환영합니다!')
    print('메뉴선택')
    print('1: 반응속도게임 | 2: 빙고게임 | 3: 프로그램 종료')
    command = int(input())

    if command == 1:
        aimlap.start_game()
        pass
    elif command == 2:
        bingo.bingo()
        pass
    elif command == 3:
        print('프로그램 종료!')
        break