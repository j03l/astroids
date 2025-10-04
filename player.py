import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.name = "player"
        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0

    def __repr__(self):
        return f"<Player @ {self.x}, {self.y}. Radius: {self.radius} Rotation: {self.rotation}>"

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # pygame.draw.polygon(
        #     surface=screen, color=Color("white"), points=self.triangle(), width=2
        # )
        pygame.gfxdraw.filled_polygon(screen, self.triangle(), pygame.Color("white"))

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.timer > 0:
            self.timer -= dt
            return

        self.timer = PLAYER_SHOOT_COOLDOWN
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

    def update(self, dt):
        super().update(dt)
        keys = pygame.key.get_pressed()
        pygame.key.set_repeat(1000, 300)

        if keys[pygame.K_a]:
            self.rotate(+dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)

        if keys[pygame.K_w]:
            self.move(+dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_HOME]:
            print(self)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)
