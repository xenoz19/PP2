import pygame
from player import MusicPlayer

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Music Player"
)

font = pygame.font.SysFont(
    None,
    36
)

player = MusicPlayer()

player.load()

running = True

while running:

    bg_path = player.get_background()

    background = pygame.image.load(
        bg_path
    )

    background = pygame.transform.scale(
        background,
        (WIDTH, HEIGHT)
    )

    screen.blit(background, (0, 0))

    text = font.render(
        f"Track: {player.playlist[player.current]}",
        True,
        (255, 255, 255)
    )

    screen.blit(text, (50, 150))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next()

            if event.key == pygame.K_b:
                player.previous()

            if event.key == pygame.K_q:
                running = False

    pygame.display.update()

pygame.quit()