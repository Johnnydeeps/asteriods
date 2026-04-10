import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    # new split method function to split and reduces size of asteroids hit by a shot.
    # Reducing from Large, Medium, Small. when Small (ASTEROID_MIN_RADIUS) is hit,
    # delete from the screen.
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        b_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        a_asteroid.velocity = a * 1.2
        b_asteroid.velocity = b * 1.2
