import pygame
import random
import os
from persistence import save_score, load_settings


def run_game():

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

    music_path = os.path.join(
        ASSETS,
        "music.mp3"
    )

    if os.path.exists(music_path):

        pygame.mixer.music.load(music_path)

        if settings["sound"]:

            pygame.mixer.music.play(-1)

        else:

            pygame.mixer.music.stop()

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

    # SCALE

    player_img = pygame.transform.scale(player_img, (50, 90))
    enemy_img = pygame.transform.scale(enemy_img, (50, 90))
    coin_img = pygame.transform.scale(coin_img, (30, 30))
    road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
    game_over_img = pygame.transform.scale(
        game_over_img,
        (WIDTH, HEIGHT)
    )

    enemy_img = pygame.transform.rotate(enemy_img, 180)

    lanes = [70, 140, 200, 270]

    LEFT_BORDER = 50
    RIGHT_BORDER = 300

    player_x = lanes[1]
    player_y = 500

    base_speed = 5
    player_speed = base_speed

    enemies = []

    for i in range(3):

        enemy = {
            "x": random.choice(lanes),
            "y": random.randint(-600, -100),
            "speed": random.randint(5, 8)
        }

        enemies.append(enemy)

    coin_x = random.choice(lanes)
    coin_y = -50

    coin_speed = 5

    coins_collected = 0

    font = pygame.font.SysFont(None, 36)

    running = True
    game_over = False

    # =============================
    # USERNAME
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
    # POWER UPS
    # =============================

    powerup_types = ["Nitro", "Shield", "Repair"]

    powerup = {
        "type": random.choice(powerup_types),
        "x": random.choice(lanes),
        "y": -150
    }

    active_powerup = None
    powerup_timer = 0
    shield_active = False

    distance = 0

    # =============================
    # RESET
    # =============================

    def reset_game():

        nonlocal player_x, player_y
        nonlocal enemies
        nonlocal coin_x, coin_y
        nonlocal coins_collected
        nonlocal game_over
        nonlocal active_powerup
        nonlocal shield_active
        nonlocal player_speed
        nonlocal distance

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

        active_powerup = None
        shield_active = False
        player_speed = base_speed
        distance = 0

        game_over = False

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

                        reset_game()

        keys = pygame.key.get_pressed()

        if not game_over:

            if keys[pygame.K_LEFT]:
                player_x -= player_speed

            if keys[pygame.K_RIGHT]:
                player_x += player_speed

            if player_x < LEFT_BORDER:
                player_x = LEFT_BORDER

            if player_x > RIGHT_BORDER:
                player_x = RIGHT_BORDER

            distance += player_speed

            if distance % 500 == 0:

                for e in enemies:
                    e["speed"] += 1

            for enemy in enemies:

                enemy["y"] += enemy["speed"]

                if enemy["y"] > HEIGHT:

                    enemy["x"] = random.choice(lanes)
                    enemy["y"] = random.randint(-600, -100)

            coin_y += coin_speed

            if coin_y > HEIGHT:

                coin_x = random.choice(lanes)
                coin_y = -50

            powerup["y"] += 4

            if powerup["y"] > HEIGHT:

                powerup["x"] = random.choice(lanes)
                powerup["y"] = -150
                powerup["type"] = random.choice(powerup_types)

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

            power_rect = pygame.Rect(
                powerup["x"],
                powerup["y"],
                40,
                40
            )

            for enemy in enemies:

                enemy_rect = pygame.Rect(
                    enemy["x"],
                    enemy["y"],
                    50,
                    90
                )

                if player_rect.colliderect(enemy_rect):

                    if shield_active:

                        shield_active = False

                    else:

                        game_over = True

                        save_score(
                            username,
                            coins_collected,
                            distance
                        )

            if player_rect.colliderect(coin_rect):

                coins_collected += 1

                coin_x = random.choice(lanes)
                coin_y = -50

            if player_rect.colliderect(power_rect):

                active_powerup = powerup["type"]

                if active_powerup == "Nitro":

                    player_speed = 10
                    powerup_timer = pygame.time.get_ticks()

                if active_powerup == "Shield":

                    shield_active = True

                if active_powerup == "Repair":

                    game_over = False

                powerup["y"] = -150

            if active_powerup == "Nitro":

                if pygame.time.get_ticks() - powerup_timer > 5000:

                    player_speed = base_speed
                    active_powerup = None

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

            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (
                    powerup["x"],
                    powerup["y"],
                    40,
                    40
                )
            )

            text = font.render(
                "Coins: " + str(coins_collected),
                True,
                (0, 0, 0)
            )

            screen.blit(text, (250, 10))

            dist_text = font.render(
                "Distance: " + str(distance),
                True,
                (0, 0, 0)
            )

            screen.blit(dist_text, (10, 10))

            if active_powerup:

                power_text = font.render(
                    "Power: " + active_powerup,
                    True,
                    (0, 0, 255)
                )

                screen.blit(power_text, (10, 40))

        pygame.display.update()

        clock.tick(60)