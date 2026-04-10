import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("================================")
    print("All gas, no brakes...pew pew pew")

    # pygame configuration
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    # "screen" variable defined as an object called from pygame library from Surface Class.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Player logic and import from player.py
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # added Groups as per lesson for organisation of objects into updatable and
    # drawable categories. Groups are a class that contains multiple objects(Classes).
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]
    Asteroid.containers = (asteroids, updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]
    AsteroidField.containers = updatable  # pyright: ignore[reportAttributeAccessIssue]
    Shot.containers = (shots, updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]

    # calling the Objects
    player = Player(x, y)
    AsteroidField()

    # Game loop logic
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
        for instance in drawable:
            instance.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
