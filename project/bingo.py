import random

# 빙고게임
##----------------------------------------------------
def bingo():
    bingoBoard = [[0 for _ in range(4)] for _ in range(4)] # 4 x 4설정
    memo = []
    bingoState = {}
    score = 0
    ##----------------------------------------------------

    for row in range(len(bingoBoard)): # 실제 행을 나타냄
        for col in range(len(bingoBoard)): # 실제 열을 나타냄
            while True:
                bingoBoard[row][col] = random.randint(1, 51)
                if bingoBoard[row][col] in memo:
                    continue
                else:
                    memo.append(bingoBoard[row][col])
                    break

    for row in bingoBoard:          # [[], [], []] => []
        for col in row:
            bingoState[col] = False

    while True:
        print('Your turn : ')
        playerPick = int(input('숫자 선택 : '))
        # 빙고보드안에 있는 숫자인지 판단
        if playerPick in memo:
            bingoBoard[playerPick] = True
            print(f'{playerPick} 색칠 완료')
        else:
            print('빙고보드에 없는 숫자임 ㅋ')
        
        for i in bingoBoard:
                for j in i:
                    if bingoBoard[j] == True:
                        print('O', end=' ')
                    else : print('X', end=' ')
                print()
                print()
        
        
        