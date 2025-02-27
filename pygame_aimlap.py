import os
import pygame
from random import randint

# 원 크기 조절
def size_down(size):
    return max(int(size * 0.985), 10)  # 최소 크기 제한

# 초기 설정
pygame.init()
current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, "images")

# 화면 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("에임 맞추기")
clock = pygame.time.Clock()

# 이미지 로드
background = pygame.image.load(os.path.join(image_path, "background.png"))
circle_img = pygame.image.load(os.path.join(image_path, "circle.png"))
hp_images = [pygame.image.load(os.path.join(image_path, f"hp{i}.png")) for i in range(1, 7)]

# 폰트 설정
game_font = pygame.font.Font(None, 40)

# 변수 설정
total_time = 30
start_ticks = pygame.time.get_ticks()
score = 0
hp = 1000
circles = []

spawn_delay = 0.5
last_spawn = 0

running = True
while running:
    dt = clock.tick(60) / 1000  # delta time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()
            for circle in circles:
                circle_rect = pygame.Rect(circle["x"], circle["y"], circle["size"], circle["size"])
                if circle_rect.collidepoint(m_pos):
                    score += 100
                    circles.remove(circle)
                    break
            else:
                hp -= 100

    # 원 생성
    if elapsed_time - last_spawn > spawn_delay:
        last_spawn = elapsed_time
        size = 100
        circles.append({
            "x": randint(50, screen_width - size - 50),
            "y": randint(50, screen_height - size - 50),
            "size": size
        })
        spawn_delay = max(0.2, spawn_delay - 0.015)  # 최소 딜레이 설정

    # 체력 상태 업데이트
    if hp <= 0:
        running = False
        game_result = "Game Over"
    
    # 화면 그리기
    screen.blit(background, (0, 0))
    for circle in circles:
        resized_circle = pygame.transform.scale(circle_img, (circle["size"], circle["size"]))
        screen.blit(resized_circle, (circle["x"], circle["y"]))

    # UI 표시
    screen.blit(game_font.render(f"Score: {score}", True, (167, 167, 167)), (10, 80))
    screen.blit(game_font.render(f"Time: {max(0, int(total_time - elapsed_time))}", True, (167, 167, 167)), (10, 115))
    screen.blit(hp_images[min(5, max(0, 5 - hp // 200))], (10, 10))

    pygame.display.update()

# 게임 종료 메시지
screen.fill((0, 0, 0))
msg = game_font.render(game_result, True, (155, 255, 255))
score_UI = game_font.render(f"Score: {score}", True, (155, 255, 255))
screen.blit(msg, (screen_width // 2 - 50, screen_height // 2 - 20))
screen.blit(score_UI, (screen_width // 2 - 75, screen_height // 2 + 20))
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()
