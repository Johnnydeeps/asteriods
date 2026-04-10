from turtle import distance  # noqa: F401

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # pyright: ignore[reportAttributeAccessIssue]
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)  # noqa: F811
        r1 = self.radius
        r2 = other.radius
        if distance <= (r1 + r2):
            return True
        else:
            return False
