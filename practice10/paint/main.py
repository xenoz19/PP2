import pygame

pygame.init()

# Размер окна
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

color = BLACK

drawing = False

mode = "brush"

start_pos = None

# Очистка экрана
screen.fill(WHITE)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Выбор инструмента
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                mode = "rectangle"

            if event.key == pygame.K_c:
                mode = "circle"

            if event.key == pygame.K_b:
                mode = "brush"

            if event.key == pygame.K_e:
                mode = "eraser"

            # Выбор цвета
            if event.key == pygame.K_1:
                color = RED

            if event.key == pygame.K_2:
                color = GREEN

            if event.key == pygame.K_3:
                color = BLUE

            if event.key == pygame.K_4:
                color = BLACK

            if event.key == pygame.K_5:
                color = YELLOW

        # Начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:

            drawing = True

            start_pos = event.pos

        # Конец рисования
        if event.type == pygame.MOUSEBUTTONUP:

            drawing = False

            end_pos = event.pos

            # Rectangle
            if mode == "rectangle":

                rect = pygame.Rect(
                    start_pos,
                    (
                        end_pos[0] - start_pos[0],
                        end_pos[1] - start_pos[1]
                    )
                )

                pygame.draw.rect(
                    screen,
                    color,
                    rect,
                    2
                )

            # Circle
            if mode == "circle":

                radius = int(
                    (
                        (
                            end_pos[0] - start_pos[0]
                        ) ** 2
                        +
                        (
                            end_pos[1] - start_pos[1]
                        ) ** 2
                    ) ** 0.5
                )

                pygame.draw.circle(
                    screen,
                    color,
                    start_pos,
                    radius,
                    2
                )

    # Brush
    if drawing and mode == "brush":

        mouse_pos = pygame.mouse.get_pos()

        pygame.draw.circle(
            screen,
            color,
            mouse_pos,
            5
        )

    # Eraser
    if drawing and mode == "eraser":

        mouse_pos = pygame.mouse.get_pos()

        pygame.draw.circle(
            screen,
            WHITE,
            mouse_pos,
            15
        )

    pygame.display.update()

    clock.tick(60)

pygame.quit()