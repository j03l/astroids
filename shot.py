import pygame
import pygame.gfxdraw

from circleshape import CircleShape
from constants import SHOT_COLOUR, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.play_sfx("fire")

    def draw(self, screen):
        # pygame.draw.circle(
        #     surface=screen,
        #     color=SHOT_COLOUR,
        #     center=self.position,
        #     radius=self.radius,
        #     width=2,
        # )
        pygame.gfxdraw.filled_circle(
            screen,
            int(self.position.x),
            int(self.position.y),
            int(self.radius),
            pygame.Color(SHOT_COLOUR),
        )

    def update(self, dt):
        self.position += self.velocity * dt
