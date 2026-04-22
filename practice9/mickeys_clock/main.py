import pygame
<<<<<<< HEAD
import datetime

pygame.init()

WIDTH = 800
HEIGHT = 800
=======
from clock import get_time_angles

pygame.init()

WIDTH = 600
HEIGHT = 600
>>>>>>> 90c314fbe17aa9ad27b561e0ef523c7fc8e7a11d

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

<<<<<<< HEAD
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
=======
hand_image = pygame.image.load(
    "images/mickey_hand.png"
>>>>>>> 90c314fbe17aa9ad27b561e0ef523c7fc8e7a11d
)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

<<<<<<< HEAD
    now = datetime.datetime.now()

    minutes = now.minute
    seconds = now.second

    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    # Вращаем руки
    minute_hand = pygame.transform.rotate(
        right_arm,
=======
    minute_angle, second_angle = get_time_angles()

    minute_hand = pygame.transform.rotate(
        hand_image,
>>>>>>> 90c314fbe17aa9ad27b561e0ef523c7fc8e7a11d
        minute_angle
    )

    second_hand = pygame.transform.rotate(
<<<<<<< HEAD
        left_arm,
        second_angle
    )

    # Рисуем фон
    screen.blit(background, (0, 0))
=======
        hand_image,
        second_angle
    )

    screen.fill((255, 255, 255))
>>>>>>> 90c314fbe17aa9ad27b561e0ef523c7fc8e7a11d

    center = (WIDTH // 2, HEIGHT // 2)

    rect1 = minute_hand.get_rect(center=center)
    rect2 = second_hand.get_rect(center=center)

    screen.blit(minute_hand, rect1)
    screen.blit(second_hand, rect2)

    pygame.display.update()

    clock.tick(1)

pygame.quit()