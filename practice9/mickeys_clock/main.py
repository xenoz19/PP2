import pygame
from clock import get_time_angles

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

hand_image = pygame.image.load(
    "images/mickey_hand.png"
)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    minute_angle, second_angle = get_time_angles()

    minute_hand = pygame.transform.rotate(
        hand_image,
        minute_angle
    )

    second_hand = pygame.transform.rotate(
        hand_image,
        second_angle
    )

    screen.fill((255, 255, 255))

    center = (WIDTH // 2, HEIGHT // 2)

    rect1 = minute_hand.get_rect(center=center)
    rect2 = second_hand.get_rect(center=center)

    screen.blit(minute_hand, rect1)
    screen.blit(second_hand, rect2)

    pygame.display.update()

    clock.tick(1)

pygame.quit()