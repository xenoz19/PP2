import pygame
import random
import os
from persistence import save_score, load_settings


def run_game():

    # =============================
    # BASIC SETTINGS
    # =============================

    WIDTH = 400
    HEIGHT = 600

    screen = pygame.display.get_surface()

    if screen is None:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Racer")

    clock = pygame.time.Clock()

    BASE_DIR = os.path.dirname(__file__)
    ASSETS = os.path.join(BASE_DIR, "assets")

    # =============================
    # LOAD SETTINGS
    # =============================

    settings = load_settings()

    # =============================
    # MUSIC
    # =============================

    pygame.mixer.init()

    music_path = os.path.join(ASSETS, "music.mp3")

    if os.path.exists(music_path):

        pygame.mixer.music.load(music_path)

        if settings["sound"]:

            pygame.mixer.music.play(-1)

    # =============================
    # LOAD IMAGES
    # =============================

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

    game_over_img = pygame.image.load(
        os.path.join(ASSETS, "game_over.png")
    )

    # =============================
    # LOAD SOUND
    # =============================


    # =============================
    # SCALE IMAGES
    # =============================

    player_img = pygame.transform.scale(player_img, (50, 90))
    enemy_img = pygame.transform.scale(enemy_img, (50, 90))
    coin_img = pygame.transform.scale(coin_img, (30, 30))
    road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
    game_over_img = pygame.transform.scale(
        game_over_img,
        (WIDTH, HEIGHT)
    )

    enemy_img = pygame.transform.rotate(enemy_img, 180)

    # =============================
    # LANES
    # =============================

    lanes = [70, 140, 200, 270]

    LEFT_BORDER = 50
    RIGHT_BORDER = 300

    # =============================
    # PLAYER
    # =============================

    player_x = lanes[1]
    player_y = 500

    base_speed = 5
    player_speed = base_speed

    # =============================
    # ENEMIES
    # =============================

    enemies = []

    for i in range(3):

        enemy = {
            "x": random.choice(lanes),
            "y": random.randint(-600, -100),
            "speed": random.randint(5, 8)
        }

        enemies.append(enemy)

    # =============================
    # COIN WITH WEIGHT
    # =============================

    coin_x = random.choice(lanes)
    coin_y = -50

    coin_speed = 5

    # RANDOM COIN VALUE
    coin_value = random.choice([1, 2, 3])

    coins_collected = 0

    font = pygame.font.SysFont(None, 36)

    running = True
    game_over = False

    # =============================
    # USERNAME INPUT
    # =============================

    username = ""

    entering_name = True

    while entering_name:

        screen.fill((0, 0, 0))

        text = font.render(
            "Enter your name:",
            True,
            (255, 255, 255)
        )

        name_surface = font.render(
            username,
            True,
            (255, 255, 255)
        )

        screen.blit(text, (90, 250))
        screen.blit(name_surface, (90, 300))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    if username != "":
                        entering_name = False

                elif event.key == pygame.K_BACKSPACE:

                    username = username[:-1]

                else:

                    username += event.unicode

    # =============================
    # GAME LOOP
    # =============================

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if game_over:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:

                        # RESET GAME
                        player_x = lanes[1]
                        coins_collected = 0
                        game_over = False

        keys = pygame.key.get_pressed()

        if not game_over:

            # =============================
            # PLAYER MOVEMENT
            # =============================

            if keys[pygame.K_LEFT]:
                player_x -= player_speed

            if keys[pygame.K_RIGHT]:
                player_x += player_speed

            if player_x < LEFT_BORDER:
                player_x = LEFT_BORDER

            if player_x > RIGHT_BORDER:
                player_x = RIGHT_BORDER

            # =============================
            # MOVE ENEMIES
            # =============================

            for enemy in enemies:

                enemy["y"] += enemy["speed"]

                if enemy["y"] > HEIGHT:

                    enemy["x"] = random.choice(lanes)

                    enemy["y"] = random.randint(-600, -100)

            # =============================
            # MOVE COIN
            # =============================

            coin_y += coin_speed

            if coin_y > HEIGHT:

                coin_x = random.choice(lanes)

                coin_y = -50

                # RANDOM NEW VALUE
                coin_value = random.choice([1, 2, 3])

            # =============================
            # COLLISION
            # =============================

            player_rect = pygame.Rect(
                player_x,
                player_y,
                50,
                90
            )

            coin_rect = pygame.Rect(
                coin_x,
                coin_y,
                30,
                30
            )

            # ENEMY COLLISION

            for enemy in enemies:

                enemy_rect = pygame.Rect(
                    enemy["x"],
                    enemy["y"],
                    50,
                    90
                )

                if player_rect.colliderect(enemy_rect):

                    game_over = True

                    save_score(
                        username,
                        coins_collected,
                        0
                    )

            # COIN COLLISION

            if player_rect.colliderect(coin_rect):

                # ADD COIN VALUE
                coins_collected += coin_value


                # INCREASE SPEED EVERY 5 COINS

                if coins_collected % 5 == 0:

                    for e in enemies:

                        e["speed"] += 1

                coin_x = random.choice(lanes)

                coin_y = -50

                coin_value = random.choice([1, 2, 3])

        # =============================
        # DRAW
        # =============================

        if game_over:

            screen.blit(game_over_img, (0, 0))

            restart_text = font.render(
                "Press R to Restart",
                True,
                (255, 255, 255)
            )

            screen.blit(restart_text, (110, 550))

        else:

            screen.blit(road_img, (0, 0))

            screen.blit(
                player_img,
                (player_x, player_y)
            )

            for enemy in enemies:

                screen.blit(
                    enemy_img,
                    (enemy["x"], enemy["y"])
                )

            screen.blit(
                coin_img,
                (coin_x, coin_y)
            )

            # SHOW COIN COUNT

            text = font.render(
                "Coins: " + str(coins_collected),
                True,
                (0, 0, 0)
            )

            screen.blit(text, (250, 10))

            # SHOW COIN VALUE

            value_text = font.render(
                "Value: " + str(coin_value),
                True,
                (0, 0, 0)
            )

            screen.blit(value_text, (10, 10))

        pygame.display.update()

        clock.tick(60)