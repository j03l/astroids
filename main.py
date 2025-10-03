import pygame

from asteroid import Asteroid
from astroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    _asteroid_field = AsteroidField()

    dt = 0

    while True:  # ma beautiful loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in asteroids:
            if player.collision(obj):
                print("Game over!")
                return

        for obj in shots:
            obj.draw(screen)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # call last !!

        dt = clock.tick(60) / 1000  # limit the framerate to 60 FPS


if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    main()
