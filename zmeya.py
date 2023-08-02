import pygame
import random
import time


pygame.init()

# Определение размеров экрана
screen_width = 800
screen_height = 600

# Определение цветов
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Змейка')

# Определение параметров змейки
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Определение параметров фрукта
fruit_pos = [random.randrange(1, (screen_width // 10)) * 10,
             random.randrange(1, (screen_height // 10)) * 10]
fruit_spawn = True

# Определение параметров игры
score = 0

# Цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Обработка нажатий клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    # Проверка некорректных движений
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Обновление позиции змейки
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10

    # Увеличение длины змейки
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (screen_width // 10)) * 10,
                     random.randrange(1, (screen_height // 10)) * 10]

    fruit_spawn = True
    screen.fill(black)

    for pos in snake_body:
        pygame.draw.rect(screen, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, white, pygame.Rect(
        fruit_pos[0], fruit_pos[1], 10, 10))

    # Проверка столкновений
    if snake_pos[0] < 0 or snake_pos[0] > screen_width - 10:
        pygame.quit()
    if snake_pos[1] < 0 or snake_pos[1] > screen_height - 10:
        pygame.quit()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()

    pygame.display.update()
    pygame.time.Clock().tick(20)