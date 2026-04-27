import pygame
import sys
from datetime import datetime

from tools import *

pygame.init()

WIDTH, HEIGHT = 1000, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

current_color = BLACK

# =========================================================
# BRUSH SIZE
# =========================================================

brush_sizes = {
    1: 2,
    2: 5,
    3: 10
}

current_brush = 2
brush_size = brush_sizes[current_brush]

# =========================================================
# TOOLS
# =========================================================

TOOL_PENCIL = "pencil"
TOOL_LINE = "line"
TOOL_RECT = "rect"
TOOL_CIRCLE = "circle"
TOOL_FILL = "fill"
TOOL_ERASER = "eraser"

TOOL_SQUARE = "square"
TOOL_RIGHT_TRIANGLE = "right_triangle"
TOOL_EQUILATERAL_TRIANGLE = "equilateral_triangle"
TOOL_RHOMBUS = "rhombus"

current_tool = TOOL_PENCIL

last_pos = None
start_pos = None
is_drawing = False

font = pygame.font.SysFont(None, 28)

# =========================================================
# SAVE FUNCTION
# =========================================================

def save_canvas():

    now = datetime.now()

    filename = now.strftime(
        "drawing_%Y-%m-%d_%H-%M-%S.png"
    )

    pygame.image.save(
        canvas,
        filename
    )

    print("Saved:", filename)


# =========================================================
# MAIN LOOP
# =========================================================

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # =================================================
        # KEYBOARD CONTROLS
        # =================================================

        if event.type == pygame.KEYDOWN:

            # Brush size
            if event.key == pygame.K_1:
                brush_size = brush_sizes[1]

            if event.key == pygame.K_2:
                brush_size = brush_sizes[2]

            if event.key == pygame.K_3:
                brush_size = brush_sizes[3]

            # Tools
            if event.key == pygame.K_p:
                current_tool = TOOL_PENCIL

            if event.key == pygame.K_l:
                current_tool = TOOL_LINE

            if event.key == pygame.K_r:
                current_tool = TOOL_RECT

            if event.key == pygame.K_c:
                current_tool = TOOL_CIRCLE

            if event.key == pygame.K_f:
                current_tool = TOOL_FILL

            if event.key == pygame.K_e:
                current_tool = TOOL_ERASER

            if event.key == pygame.K_q:
                current_tool = TOOL_SQUARE

            if event.key == pygame.K_t:
                current_tool = TOOL_RIGHT_TRIANGLE

            if event.key == pygame.K_y:
                current_tool = TOOL_EQUILATERAL_TRIANGLE

            if event.key == pygame.K_h:
                current_tool = TOOL_RHOMBUS

            # Save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()

        # =================================================
        # MOUSE DOWN
        # =================================================

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            is_drawing = True
            start_pos = (x, y)
            last_pos = (x, y)

            if current_tool == TOOL_FILL:

                flood_fill(
                    canvas,
                    x,
                    y,
                    current_color
                )

        # =================================================
        # MOUSE MOTION
        # =================================================

        if event.type == pygame.MOUSEMOTION:

            if is_drawing:

                x, y = event.pos

                if current_tool == TOOL_PENCIL:

                    pygame.draw.line(
                        canvas,
                        current_color,
                        last_pos,
                        (x, y),
                        brush_size
                    )

                    last_pos = (x, y)

                if current_tool == TOOL_ERASER:

                    pygame.draw.line(
                        canvas,
                        WHITE,
                        last_pos,
                        (x, y),
                        brush_size
                    )

                    last_pos = (x, y)

        # =================================================
        # MOUSE UP
        # =================================================

        if event.type == pygame.MOUSEBUTTONUP:

            is_drawing = False

            x, y = event.pos

            if current_tool == TOOL_LINE:

                draw_line(
                    canvas,
                    current_color,
                    start_pos,
                    (x, y),
                    brush_size
                )

            if current_tool == TOOL_RECT:

                draw_rectangle(
                    canvas,
                    current_color,
                    start_pos,
                    (x, y),
                    brush_size
                )

            if current_tool == TOOL_CIRCLE:

                draw_circle(
                    canvas,
                    current_color,
                    start_pos,
                    (x, y),
                    brush_size
                )

            if current_tool == TOOL_SQUARE:

                draw_square(
                    canvas,
                    current_color,
                    start_pos,
                    (x, y),
                    brush_size
                )

            if current_tool == TOOL_RIGHT_TRIANGLE:

                draw_right_triangle(
                    canvas,
                    current_color,
                    start_pos,
                    (x, y),
                    brush_size
                )

            if current_tool == TOOL_EQUILATERAL_TRIANGLE:

                draw_equilateral_triangle(
                    canvas,
                    current_color,
                    start_pos,
                    (x, y),
                    brush_size
                )

            if current_tool == TOOL_RHOMBUS:

                draw_rhombus(
                    canvas,
                    current_color,
                    start_pos,
                    (x, y),
                    brush_size
                )

    screen.fill(WHITE)

    screen.blit(canvas, (0, 0))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()