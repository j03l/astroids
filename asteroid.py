from random import choice, uniform

import pygame
import pygame.gfxdraw

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, spawn, color):
        super().__init__(x, y, radius)
        self._spawn = spawn  # injected factory
        self.color = color

    def draw(self, screen):
        # pygame.draw.circle(
        #     surface=screen,
        #     color=self.color,
        #     center=self.position,
        #     radius=self.radius,
        #     width=2,
        # )
        pygame.gfxdraw.filled_circle(
            screen,
            int(self.position.x),
            int(self.position.y),
            int(self.radius),
            pygame.Color(self.color),
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:  # small asteroid
            return

        random_angle = uniform(20, 50)
        v1 = self.velocity.rotate(random_angle) * 1.2
        v2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        self._spawn(new_radius, self.position, v1, self.color)
        self._spawn(new_radius, self.position, v2, self.color)
