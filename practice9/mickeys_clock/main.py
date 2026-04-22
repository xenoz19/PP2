import pygame
import datetime

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# Фон часов (без рук)
background = pygame.image.load(
    "images/mainclock.png"
)

background = pygame.transform.scale(
    background,
    (WIDTH, HEIGHT)
)

# Руки
left_arm = pygame.image.load(
    "images/leftarm.png"
)

right_arm = pygame.image.load(
    "images/rightarm.png"
)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()

    minutes = now.minute
    seconds = now.second

    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    # Вращаем руки
    minute_hand = pygame.transform.rotate(
        right_arm,
        minute_angle
    )

    second_hand = pygame.transform.rotate(
        left_arm,
        second_angle
    )

    # Рисуем фон
    screen.blit(background, (0, 0))

    center = (WIDTH // 2, HEIGHT // 2)

    rect1 = minute_hand.get_rect(center=center)
    rect2 = second_hand.get_rect(center=center)

    screen.blit(minute_hand, rect1)
    screen.blit(second_hand, rect2)

    pygame.display.update()

    clock.tick(1)

pygame.quit()