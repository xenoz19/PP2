import pygame

class Ball:

    def __init__(self, x, y, radius=25, speed=20):

        self.x = x
        self.y = y

        self.radius = radius
        self.speed = speed

    def move(self, key, width, height):

        if key == pygame.K_UP:
            if self.y - self.speed - self.radius >= 0:
                self.y -= self.speed

        if key == pygame.K_DOWN:
            if self.y + self.speed + self.radius <= height:
                self.y += self.speed

        if key == pygame.K_LEFT:
            if self.x - self.speed - self.radius >= 0:
                self.x -= self.speed

        if key == pygame.K_RIGHT:
            if self.x + self.speed + self.radius <= width:
                self.x += self.speed

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (self.x, self.y),
            self.radius
        )