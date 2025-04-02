import pygame
import random
import time

# 初始化pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# 设置游戏窗口
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")

# 游戏时钟
clock = pygame.time.Clock()

# 蛇的初始位置和方向
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)

# 食物位置
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# 分数
score = 0
font = pygame.font.SysFont('Arial', 24)

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_s and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_a and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_d and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # 移动蛇
    head_x, head_y = snake[0]
    dir_x, dir_y = snake_direction
    new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)

    # 碰撞检测
    if new_head in snake:
        # 游戏结束
        time.sleep(1)
        snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        snake_direction = (1, 0)
        score = 0
    else:
        snake.insert(0, new_head)

        # 吃食物
        if new_head == food:
            score += 10
            food = (random.randint(0, GRID_WIDTH - 1),
                    random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

    # 绘制
    screen.fill(BLACK)

    # 绘制食物
    food_x, food_y = food
    pygame.draw.rect(screen, RED, (food_x * GRID_SIZE,
                     food_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # 绘制蛇
    for i, (x, y) in enumerate(snake):
        color = GREEN if i == 0 else GRAY
        pygame.draw.rect(screen, color, (x * GRID_SIZE, y *
                         GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # 绘制分数
    score_text = font.render(f"得分: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
