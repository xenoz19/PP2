import pygame
import random
import os

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(__file__)
ASSETS = os.path.join(BASE_DIR, "assets")

# Загрузка изображений
player_img = pygame.image.load(
    os.path.join(ASSETS, "player_car.png")
)

enemy_img = pygame.image.load(
    os.path.join(ASSETS, "enemy_car.png")
)

coin_img = pygame.image.load(
    os.path.join(ASSETS, "coin.png")
)

road_img = pygame.image.load(
    os.path.join(ASSETS, "road.png")
)

# NEW — Game Over картинка
game_over_img = pygame.image.load(
    os.path.join(ASSETS, "game_over.png")
)

# Масштабирование
player_img = pygame.transform.scale(player_img, (50, 90))
enemy_img = pygame.transform.scale(enemy_img, (50, 90))
coin_img = pygame.transform.scale(coin_img, (30, 30))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

game_over_img = pygame.transform.scale(
    game_over_img,
    (WIDTH, HEIGHT)
)

# Поворот машин
player_img = pygame.transform.rotate(player_img, 360)
enemy_img = pygame.transform.rotate(enemy_img, 180)

# Полосы дороги
lanes = [70, 140, 200, 270]

LEFT_BORDER = 50
RIGHT_BORDER = 350 - 50

# Игрок
player_x = lanes[1]
player_y = 500

player_speed = 5

# Враги
enemies = []

for i in range(3):

    enemy = {
        "x": random.choice(lanes),
        "y": random.randint(-600, -100),
        "speed": random.randint(5, 8)
    }

    enemies.append(enemy)

# Монета
coin_x = random.choice(lanes)
coin_y = -50

coin_speed = 5

coins_collected = 0

font = pygame.font.SysFont(None, 36)

running = True
game_over = False


# Функция перезапуска игры
def reset_game():

    global player_x, player_y
    global enemies
    global coin_x, coin_y
    global coins_collected
    global game_over

    player_x = lanes[1]
    player_y = 500

    enemies.clear()

    for i in range(3):

        enemy = {
            "x": random.choice(lanes),
            "y": random.randint(-600, -100),
            "speed": random.randint(5, 8)
        }

        enemies.append(enemy)

    coin_x = random.choice(lanes)
    coin_y = -50

    coins_collected = 0

    game_over = False


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Restart
        if game_over:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:

                    reset_game()

    keys = pygame.key.get_pressed()

    if not game_over:

        # Движение
        if keys[pygame.K_LEFT]:
            player_x -= player_speed

        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        if keys[pygame.K_UP]:
            player_y -= player_speed

        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Ограничение по дороге
        if player_x < LEFT_BORDER:
            player_x = LEFT_BORDER

        if player_x > RIGHT_BORDER:
            player_x = RIGHT_BORDER

        if player_y < 0:
            player_y = 0

        if player_y > HEIGHT - 90:
            player_y = HEIGHT - 90

        # Движение врагов
        for enemy in enemies:

            enemy["y"] += enemy["speed"]

            if enemy["y"] > HEIGHT:

                enemy["x"] = random.choice(lanes)

                enemy["y"] = random.randint(-600, -100)

                enemy["speed"] = random.randint(5, 8)

        # Движение монеты
        coin_y += coin_speed

        if coin_y > HEIGHT:

            coin_x = random.choice(lanes)
            coin_y = -50

        # Rectangles
        player_rect = pygame.Rect(player_x, player_y, 50, 90)
        coin_rect = pygame.Rect(coin_x, coin_y, 30, 30)

        # Collision
        for enemy in enemies:

            enemy_rect = pygame.Rect(
                enemy["x"],
                enemy["y"],
                50,
                90
            )

            if player_rect.colliderect(enemy_rect):

                print("GAME OVER")

                game_over = True

        # Сбор монеты
        if player_rect.colliderect(coin_rect):

            coins_collected += 1

            coin_x = random.choice(lanes)
            coin_y = -50

    # Рисуем
    if game_over:

        screen.blit(game_over_img, (0, 0))

        restart_text = font.render(
            "Press R to Restart",
            True,
            (255, 255, 255)
        )

        screen.blit(
            restart_text,
            (110, 550)
        )

    else:

        screen.blit(road_img, (0, 0))

        screen.blit(player_img, (player_x, player_y))

        for enemy in enemies:

            screen.blit(
                enemy_img,
                (enemy["x"], enemy["y"])
            )

        screen.blit( 
            coin_img,
            (coin_x, coin_y)
        )

        text = font.render(
            "Coins: " + str(coins_collected),
            True,
            (0, 0, 0)
        )

        screen.blit(text, (250, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()