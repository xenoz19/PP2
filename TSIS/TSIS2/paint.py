
# =========================================================
# FILE: paint.py
# =========================================================

import pygame
import sys
from datetime import datetime

# импортируем функции из tools.py
from tools import flood_fill, draw_line, draw_rectangle, draw_circle

pygame.init()

WIDTH, HEIGHT = 1000, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Paint Application")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

current_color = BLACK

# ===============================
# BRUSH SIZE
# ===============================

brush_sizes = {
    1: 2,
    2: 5,
    3: 10
}

current_brush = 2
brush_size = brush_sizes[current_brush]

# ===============================
# TOOLS
# ===============================

TOOL_PENCIL = "pencil"
TOOL_LINE = "line"
TOOL_RECT = "rect"
TOOL_CIRCLE = "circle"
TOOL_FILL = "fill"
TOOL_ERASER = "eraser"

current_tool = TOOL_PENCIL

last_pos = None
start_pos = None
is_drawing = False

font = pygame.font.SysFont(None, 28)
text_input = ""
text_position = None
text_active = False


# ===============================
# SAVE FUNCTION
# ===============================

def save_canvas():

    now = datetime.now()

    filename = now.strftime("drawing_%Y-%m-%d_%H-%M-%S.png")

    pygame.image.save(canvas, filename)

    print("Saved:", filename)


# ===============================
# MAIN LOOP
# ===============================

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # ===============================
        # KEYBOARD
        # ===============================

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                current_brush = 1
                brush_size = brush_sizes[current_brush]

            if event.key == pygame.K_2:
                current_brush = 2
                brush_size = brush_sizes[current_brush]

            if event.key == pygame.K_3:
                current_brush = 3
                brush_size = brush_sizes[current_brush]

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

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()

            # TEXT TOOL

            if text_active:

                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_input, True, current_color)
                    canvas.blit(text_surface, text_position)

                    text_input = ""
                    text_active = False

                elif event.key == pygame.K_ESCAPE:
                    text_input = ""
                    text_active = False

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        # ===============================
        # MOUSE DOWN
        # ===============================

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            is_drawing = True
            start_pos = (x, y)
            last_pos = (x, y)

            if current_tool == TOOL_FILL:
                flood_fill(canvas, x, y, current_color)

            if current_tool == "text":
                text_position = (x, y)
                text_active = True
                text_input = ""

        # ===============================
        # MOUSE MOTION
        # ===============================

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

                # ERASER
                if current_tool == TOOL_ERASER:

                    pygame.draw.line(
                        canvas,
                        WHITE,
                        last_pos,
                        (x, y),
                        brush_size
                    )

                    last_pos = (x, y)

        # ===============================
        # MOUSE UP
        # ===============================

        if event.type == pygame.MOUSEBUTTONUP:

            is_drawing = False

            x, y = event.pos

            if current_tool == TOOL_LINE:
                draw_line(canvas, current_color, start_pos, (x, y), brush_size)

            if current_tool == TOOL_RECT:
                draw_rectangle(canvas, current_color, start_pos, (x, y), brush_size)

            if current_tool == TOOL_CIRCLE:
                draw_circle(canvas, current_color, start_pos, (x, y), brush_size)

    screen.fill(WHITE)

    screen.blit(canvas, (0, 0))

    if is_drawing and current_tool == TOOL_LINE:

        mouse_pos = pygame.mouse.get_pos()

        pygame.draw.line(
            screen,
            current_color,
            start_pos,
            mouse_pos,
            brush_size
        )

    if text_active:

        text_surface = font.render(text_input, True, current_color)
        screen.blit(text_surface, text_position)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
