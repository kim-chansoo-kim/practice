import random

def bingo():
    SIZE = 4  # 4x4 빙고
    bingoBoard = [[0] * SIZE for _ in range(SIZE)]  # 빙고판
    bingoState = {}  # 숫자 체크 상태
    score = 0  # 빙고 점수
    
    # 1️⃣ 1~51 사이에서 중복 없이 16개 숫자 뽑기
    numbers = random.sample(range(1, 51), SIZE * SIZE)
    
    # 2️⃣ 빙고판에 숫자 채우기 & 상태 초기화
    index = 0
    for row in range(SIZE):
        for col in range(SIZE):
            bingoBoard[row][col] = numbers[index]
            bingoState[numbers[index]] = False
            index += 1

    # 3️⃣ 빙고판 출력 함수
    def print_board():
        for row in bingoBoard:
            for num in row:
                print("O" if bingoState[num] else "X", end=" ")
            print()
        print()

    # 4️⃣ 빙고 체크 함수
    def check_bingo():
        nonlocal score
        new_score = 0  # 한 번에 중복 점수 방지

        # 가로 체크
        for row in bingoBoard:
            if all(bingoState[num] for num in row):
                new_score += 1

        # 세로 체크
        for col in range(SIZE):
            if all(bingoState[bingoBoard[row][col]] for row in range(SIZE)):
                new_score += 1

        # 대각선 체크
        if all(bingoState[bingoBoard[i][i]] for i in range(SIZE)):
            new_score += 1
        if all(bingoState[bingoBoard[i][SIZE - 1 - i]] for i in range(SIZE)):
            new_score += 1

        if new_score > score:
            score = new_score
            print(f"현재 빙고 개수: {score}")

    # 5️⃣ 게임 루프
    while True:
        try:
            print("Your turn")
            playerPick = int(input("숫자 선택: "))

            if playerPick in bingoState:
                if not bingoState[playerPick]:  # 중복 체크 방지
                    bingoState[playerPick] = True
                    print(f"{playerPick} 색칠 완료!")
                    print_board()
                    check_bingo()
                else:
                    print("이미 선택한 숫자입니다!")
            else:
                print("빙고판에 없는 숫자입니다!\n")

            if score >= 3:  # 3줄 완성 시 게임 종료
                print("🎉 게임 클리어! 🎉")
                break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요!")

# 실행
if __name__ == "__main__":
    bingo()
