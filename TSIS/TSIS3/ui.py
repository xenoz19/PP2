import pygame
from racer import run_game
from persistence import load_leaderboard, load_settings, save_settings

WIDTH = 400
HEIGHT = 600


def main_menu():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 40)

    running = True

    while running:

        screen.fill((0, 0, 0))

        title = font.render("RACER GAME", True, (255, 255, 255))
        play = font.render("1 - Play", True, (255, 255, 255))
        leaderboard = font.render("2 - Leaderboard", True, (255, 255, 255))
        settings = font.render("3 - Settings", True, (255, 255, 255))
        quit_text = font.render("4 - Quit", True, (255, 255, 255))

        screen.blit(title, (100, 150))
        screen.blit(play, (120, 250))
        screen.blit(leaderboard, (120, 300))
        screen.blit(settings, (120, 350))
        screen.blit(quit_text, (120, 400))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:

                    run_game()

                if event.key == pygame.K_2:

                    leaderboard_screen()

                if event.key == pygame.K_3:

                    settings_screen()

                if event.key == pygame.K_4:

                    running = False


def leaderboard_screen():

    screen = pygame.display.get_surface()
    font = pygame.font.SysFont(None, 32)

    data = load_leaderboard()

    running = True

    while running:

        screen.fill((0, 0, 0))

        y = 100

        for i, score in enumerate(data):

            text = font.render(
                f"{i+1}. {score['name']} "
                f"{score['coins']} coins "
                f"{score['distance']} m",
                True,
                (255, 255, 255)
            )

            screen.blit(text, (50, y))

            y += 40

        back = font.render(
            "Press ESC to go back",
            True,
            (255, 255, 255)
        )

        screen.blit(back, (80, 500))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    running = False


def settings_screen():

    screen = pygame.display.get_surface()
    font = pygame.font.SysFont(None, 32)

    settings = load_settings()

    running = True

    while running:

        screen.fill((0, 0, 0))

        text1 = font.render(
            f"Difficulty: {settings['difficulty']}",
            True,
            (255, 255, 255)
        )

        text2 = font.render(
            f"Sound: {settings['sound']}",
            True,
            (255, 255, 255)
        )

        info = font.render(
            "Press D or S to change",
            True,
            (255, 255, 255)
        )

        back = font.render(
            "ESC - Back",
            True,
            (255, 255, 255)
        )

        screen.blit(text1, (80, 200))
        screen.blit(text2, (80, 250))
        screen.blit(info, (80, 320))
        screen.blit(back, (80, 500))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:

                    if settings["difficulty"] == "normal":
                        settings["difficulty"] = "hard"
                    else:
                        settings["difficulty"] = "normal"

                    save_settings(settings)

                if event.key == pygame.K_s:

                    settings["sound"] = not settings["sound"]

                    save_settings(settings)

                if event.key == pygame.K_ESCAPE:

                    running = False