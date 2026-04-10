import pygame

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


# inheritance and Player class constructor
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.shot_cooldown_timer = 0

    # Turn the Player class (which is a circle) into a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Put the modified Player class (now a triangle) on the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # method function to rotate the triangle(Player)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # method function to move the triangle(Player)
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # method function to shoot
    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return

        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)  # pyright: ignore[reportAttributeAccessIssue]
        shot_vector = pygame.Vector2(0, 1)
        rotated_shot = shot_vector.rotate(self.rotation)
        rotated_with_speed_shot = rotated_shot * PLAYER_SHOOT_SPEED
        shot.velocity = rotated_with_speed_shot

    # method function to update what the trianlge (Player) is doing on screen with inputs A and D
    # for rotation. Inputs W and S for moving. Inputs SPACEBAR for shooting.
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shot_cooldown_timer -= dt
