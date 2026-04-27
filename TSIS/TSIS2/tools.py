# ===============================
# Project Structure for TSIS2
# ===============================
# TSIS2/
# ├── paint.py
# ├── tools.py
# └── assets/
#
# Ниже приведён код для ДВУХ файлов, как требуют в задании.
# Просто скопируй соответствующие части в отдельные файлы.

# =========================================================
# FILE: tools.py
# =========================================================

import pygame
from collections import deque

WIDTH, HEIGHT = 1000, 700

WHITE = (255, 255, 255)

# ===============================
# FLOOD FILL FUNCTION
# ===============================

def flood_fill(surface, x, y, new_color):
    """
    Flood fill алгоритм.
    Использует очередь deque для обхода пикселей.
    """

    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:

        px, py = queue.popleft()

        if px < 0 or px >= WIDTH or py < 0 or py >= HEIGHT:
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        queue.append((px + 1, py))
        queue.append((px - 1, py))
        queue.append((px, py + 1))
        queue.append((px, py - 1))


# ===============================
# DRAW SHAPES FUNCTIONS
# ===============================

def draw_line(surface, color, start_pos, end_pos, brush_size):
    pygame.draw.line(surface, color, start_pos, end_pos, brush_size)


def draw_rectangle(surface, color, start_pos, end_pos, brush_size):

    rect = pygame.Rect(
        start_pos[0],
        start_pos[1],
        end_pos[0] - start_pos[0],
        end_pos[1] - start_pos[1]
    )

    pygame.draw.rect(surface, color, rect, brush_size)


def draw_circle(surface, color, start_pos, end_pos, brush_size):

    radius = int(
        ((end_pos[0] - start_pos[0]) ** 2 +
         (end_pos[1] - start_pos[1]) ** 2) ** 0.5
    )

    pygame.draw.circle(
        surface,
        color,
        start_pos,
        radius,
        brush_size
    )

