import pygame
import sys
from datetime import datetime

from tools import *

pygame.init()

WIDTH, HEIGHT = 1000, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS2 Paint")

# =========================
# PALETTE
# =========================

PALETTE_COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (255, 192, 203),
    (128, 0, 128),
    (0, 255, 255),
    (255, 255, 255)
]

PALETTE_SIZE = 40
PALETTE_MARGIN = 5

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

current_color = PALETTE_COLORS[0]

# =========================
# BRUSH
# =========================

brush_sizes = {1: 2, 2: 5, 3: 10}
brush_size = brush_sizes[2]

# =========================
# TOOLS
# =========================

TOOL_PENCIL = "pencil"
TOOL_LINE = "line"
TOOL_RECT = "rect"
TOOL_CIRCLE = "circle"
TOOL_FILL = "fill"
TOOL_ERASER = "eraser"
TOOL_TEXT = "text"

TOOL_SQUARE = "square"
TOOL_RIGHT_TRIANGLE = "right_triangle"
TOOL_EQUILATERAL_TRIANGLE = "equilateral_triangle"
TOOL_RHOMBUS = "rhombus"

current_tool = TOOL_PENCIL

last_pos = None
start_pos = None
is_drawing = False

font = pygame.font.SysFont(None, 28)

# =========================
# TEXT STATE
# =========================

text_active = False
text_input = ""
text_pos = (0, 0)

# =========================
# SAVE
# =========================

def save_canvas():
    filename = datetime.now().strftime("drawing_%Y-%m-%d_%H-%M-%S.png")
    pygame.image.save(canvas, filename)
    print("Saved:", filename)

# =========================
# UI
# =========================

def draw_palette(screen):
    for i, color in enumerate(PALETTE_COLORS):
        x = i * (PALETTE_SIZE + PALETTE_MARGIN)
        rect = pygame.Rect(x, 0, PALETTE_SIZE, PALETTE_SIZE)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

def draw_instructions(screen, font):
    lines = [
        "P/L/R/C/F/E - Tools | Q/T/Y/H - Shapes | X - Text",
        "Enter - Apply | Esc - Cancel | 1/2/3 - Brush | Ctrl+S - Save"
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (10, HEIGHT - 60 + i * 20))

# =========================
# MAIN LOOP
# =========================

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # =========================
        # KEYBOARD
        # =========================

        if event.type == pygame.KEYDOWN:

            # TEXT MODE
            if text_active:

                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_input, True, current_color)
                    canvas.blit(text_surface, text_pos)
                    text_active = False
                    text_input = ""

                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

                continue

            # tools
            if event.key == pygame.K_p:
                current_tool = TOOL_PENCIL
            elif event.key == pygame.K_l:
                current_tool = TOOL_LINE
            elif event.key == pygame.K_r:
                current_tool = TOOL_RECT
            elif event.key == pygame.K_c:
                current_tool = TOOL_CIRCLE
            elif event.key == pygame.K_f:
                current_tool = TOOL_FILL
            elif event.key == pygame.K_e:
                current_tool = TOOL_ERASER
            elif event.key == pygame.K_q:
                current_tool = TOOL_SQUARE
            elif event.key == pygame.K_t:
                current_tool = TOOL_RIGHT_TRIANGLE
            elif event.key == pygame.K_y:
                current_tool = TOOL_EQUILATERAL_TRIANGLE
            elif event.key == pygame.K_h:
                current_tool = TOOL_RHOMBUS
            elif event.key == pygame.K_x:
                current_tool = TOOL_TEXT

            # brush
            if event.key == pygame.K_1:
                brush_size = brush_sizes[1]
            if event.key == pygame.K_2:
                brush_size = brush_sizes[2]
            if event.key == pygame.K_3:
                brush_size = brush_sizes[3]

            # save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()

        # =========================
        # MOUSE
        # =========================

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            # palette
            if y <= PALETTE_SIZE:
                index = x // (PALETTE_SIZE + PALETTE_MARGIN)
                if index < len(PALETTE_COLORS):
                    current_color = PALETTE_COLORS[index]
                continue

            y -= (PALETTE_SIZE + PALETTE_MARGIN)

            if y < 0 or y >= HEIGHT:
                continue

            #  TEXT TOOL
            if current_tool == TOOL_TEXT:
                text_active = True
                text_input = ""
                text_pos = (x, y)
                continue

            is_drawing = True
            start_pos = (x, y)
            last_pos = (x, y)

            if current_tool == TOOL_FILL:
                flood_fill(canvas, x, y, current_color)

        # =========================
        # DRAWING
        # =========================

        if event.type == pygame.MOUSEMOTION and is_drawing:

            x, y = event.pos
            y -= (PALETTE_SIZE + PALETTE_MARGIN)

            if y < 0:
                continue

            if current_tool == TOOL_PENCIL:
                pygame.draw.line(canvas, current_color, last_pos, (x, y), brush_size)
                last_pos = (x, y)

            if current_tool == TOOL_ERASER:
                pygame.draw.line(canvas, (255, 255, 255), last_pos, (x, y), brush_size)
                last_pos = (x, y)

        if event.type == pygame.MOUSEBUTTONUP:

            is_drawing = False

            x, y = event.pos
            y -= (PALETTE_SIZE + PALETTE_MARGIN)

            if y < 0:
                continue

            if current_tool == TOOL_LINE:
                draw_line(canvas, current_color, start_pos, (x, y), brush_size)
            if current_tool == TOOL_RECT:
                draw_rectangle(canvas, current_color, start_pos, (x, y), brush_size)
            if current_tool == TOOL_CIRCLE:
                draw_circle(canvas, current_color, start_pos, (x, y), brush_size)
            if current_tool == TOOL_SQUARE:
                draw_square(canvas, current_color, start_pos, (x, y), brush_size)
            if current_tool == TOOL_RIGHT_TRIANGLE:
                draw_right_triangle(canvas, current_color, start_pos, (x, y), brush_size)
            if current_tool == TOOL_EQUILATERAL_TRIANGLE:
                draw_equilateral_triangle(canvas, current_color, start_pos, (x, y), brush_size)
            if current_tool == TOOL_RHOMBUS:
                draw_rhombus(canvas, current_color, start_pos, (x, y), brush_size)

    # =========================
    # RENDER
    # =========================

    screen.fill((255, 255, 255))
    screen.blit(canvas, (0, PALETTE_SIZE + PALETTE_MARGIN))

    draw_palette(screen)
    draw_instructions(screen, font)

    # TEXT PREVIEW
    if text_active:
        preview = font.render(text_input, True, current_color)
        screen.blit(
            preview,
            (text_pos[0], text_pos[1] + PALETTE_SIZE + PALETTE_MARGIN)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()