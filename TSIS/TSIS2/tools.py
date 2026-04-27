import pygame
from collections import deque

# Screen size
WIDTH, HEIGHT = 1000, 700

WHITE = (255, 255, 255)

# =========================================================
# FLOOD FILL FUNCTION
# =========================================================

def flood_fill(surface, x, y, new_color):
    """
    Flood fill algorithm using queue (BFS).
    Fills connected area with selected color.
    """

    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:

        px, py = queue.popleft()

        # Check boundaries
        if px < 0 or px >= WIDTH or py < 0 or py >= HEIGHT:
            continue

        # Check color match
        if surface.get_at((px, py)) != target_color:
            continue

        # Fill pixel
        surface.set_at((px, py), new_color)

        # Add neighbors
        queue.append((px + 1, py))
        queue.append((px - 1, py))
        queue.append((px, py + 1))
        queue.append((px, py - 1))


# =========================================================
# BASIC SHAPES
# =========================================================

def draw_line(surface, color, start_pos, end_pos, brush_size):

    pygame.draw.line(
        surface,
        color,
        start_pos,
        end_pos,
        brush_size
    )


def draw_rectangle(surface, color, start_pos, end_pos, brush_size):

    rect = pygame.Rect(
        start_pos[0],
        start_pos[1],
        end_pos[0] - start_pos[0],
        end_pos[1] - start_pos[1]
    )

    pygame.draw.rect(
        surface,
        color,
        rect,
        brush_size
    )


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


# =========================================================
# REQUIRED SHAPES FOR TSIS2
# =========================================================

def draw_square(surface, color, start_pos, end_pos, brush_size):
    """
    Draw square (equal width and height)
    """

    size = min(
        abs(end_pos[0] - start_pos[0]),
        abs(end_pos[1] - start_pos[1])
    )

    rect = pygame.Rect(
        start_pos[0],
        start_pos[1],
        size,
        size
    )

    pygame.draw.rect(
        surface,
        color,
        rect,
        brush_size
    )


def draw_right_triangle(surface, color, start_pos, end_pos, brush_size):
    """
    Draw right triangle
    """

    x1, y1 = start_pos
    x2, y2 = end_pos

    points = [
        (x1, y1),
        (x1, y2),
        (x2, y2)
    ]

    pygame.draw.polygon(
        surface,
        color,
        points,
        brush_size
    )


def draw_equilateral_triangle(surface, color, start_pos, end_pos, brush_size):
    """
    Draw equilateral triangle
    """

    x1, y1 = start_pos
    x2, y2 = end_pos

    base = abs(x2 - x1)

    height = int(base * 0.866)

    points = [
        (x1, y2),
        (x2, y2),
        ((x1 + x2) // 2, y2 - height)
    ]

    pygame.draw.polygon(
        surface,
        color,
        points,
        brush_size
    )


def draw_rhombus(surface, color, start_pos, end_pos, brush_size):
    """
    Draw rhombus
    """

    x1, y1 = start_pos
    x2, y2 = end_pos

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    points = [
        (center_x, y1),
        (x2, center_y),
        (center_x, y2),
        (x1, center_y)
    ]

    pygame.draw.polygon(
        surface,
        color,
        points,
        brush_size
    )