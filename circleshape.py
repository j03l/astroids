import pygame

from constants import SOUND_EFFECTS


class CircleShape(pygame.sprite.Sprite):
    """Base class for the shape of players and characters."""

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, circle):
        distance = self.position.distance_to(circle.position)
        if distance <= self.radius + circle.radius:
            return True
        return False

    def play_sfx(self, sfx):
        """Play a specific sound effect."""
        sound = pygame.mixer.Sound(SOUND_EFFECTS[sfx])
        sound.play()
