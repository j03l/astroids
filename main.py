import pygame

from asteroid import Asteroid
from astroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot
from ui import Interface


class State:
    def __init__(self):
        self.dt = 0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def start(self):
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroid_field = AsteroidField()
        self.interface = Interface(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        return self.player, self.asteroid_field

    def restart(self, groups):
        for group in groups:
            for obj in group:
                obj.kill()
        return self.start()


def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    state = State()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    interface = pygame.sprite.Group()
    groups = [
        interface,
        drawable,
        updatable,
        asteroids,
        shots,
    ]

    Interface.containers = interface
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    state.start()

    while True:  # ma beautiful loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(state.dt)

        if state.player.out_of_bounds():
            print("You left the screen!")
            state.restart(groups)

        state.screen.fill("black")

        for asteroid in asteroids:
            if state.player.collision(asteroid):
                print("Game over!")
                state.restart(groups)

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        for obj in shots:
            obj.draw(state.screen)

        for obj in drawable:
            obj.draw(state.screen)

        # for obj in interface:
        #     obj.draw(state.screen)

        pygame.display.flip()  # call last !!

        state.dt = state.clock.tick(60) / 1000  # limit the framerate to 60 FPS


if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    main()
