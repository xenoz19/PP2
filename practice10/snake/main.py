import pygame
import random
import os

pygame.init()

# Размер окна
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Путь к assets
BASE_DIR = os.path.dirname(__file__)
ASSETS = os.path.join(BASE_DIR, "assets")

# Загрузка картинки еды
food_img = pygame.image.load(
    os.path.join(ASSETS, "food.png")
)

food_img = pygame.transform.scale(
    food_img,
    (20, 20)
)

# Размер блока
BLOCK = 10

# Начальная скорость
snake_speed = 10

# Шрифт
font = pygame.font.SysFont(None, 30)

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Генерация еды
def generate_food(snake):

    while True:

        x = random.randrange(
            0,
            WIDTH,
            BLOCK
        )

        y = random.randrange(
            0,
            HEIGHT,
            BLOCK
        )

        # Проверка чтобы еда не появилась на змейке
        if (x, y) not in snake:
            return x, y


# Начальная змейка
snake = [(100, 100)]

direction = "RIGHT"

# Первая еда
food_x, food_y = generate_food(snake)

score = 0
level = 1

running = True

while running:

    # События
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                direction = "LEFT"

            if event.key == pygame.K_RIGHT:
                direction = "RIGHT"

            if event.key == pygame.K_UP:
                direction = "UP"

            if event.key == pygame.K_DOWN:
                direction = "DOWN"

    # Голова змейки
    head_x, head_y = snake[0]

    # Движение
    if direction == "LEFT":
        head_x -= BLOCK

    if direction == "RIGHT":
        head_x += BLOCK

    if direction == "UP":
        head_y -= BLOCK

    if direction == "DOWN":
        head_y += BLOCK

    new_head = (head_x, head_y)

    # Проверка выхода за границы
    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
    ):
        print("GAME OVER")
        running = False

    # Проверка столкновения с собой
    if new_head in snake:
        print("GAME OVER")
        running = False

    # Добавляем голову
    snake.insert(0, new_head)

    # Если съели еду
    if new_head == (food_x, food_y):

        score += 1

        # Новый уровень каждые 3 еды
        if score % 3 == 0:

            level += 1

            snake_speed += 2

        food_x, food_y = generate_food(snake)

    else:

        snake.pop()

    # Очистка экрана
    screen.fill(WHITE)

    # Рисуем змейку
    for segment in snake:

        pygame.draw.rect(
            screen,
            GREEN,
            (
                segment[0],
                segment[1],
                BLOCK,
                BLOCK
            )
        )

    # Рисуем еду (картинка)
    screen.blit(
        food_img,
        (food_x, food_y)
    )

    # Текст Score
    score_text = font.render(
        "Score: " + str(score),
        True,
        BLACK
    )

    # Текст Level
    level_text = font.render(
        "Level: " + str(level),
        True,
        BLACK
    )

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()