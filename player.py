import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS


# inheritance and Player class constructor
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

    # Turn the Player class (which is a circle) into a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Put the modified Player class on the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
