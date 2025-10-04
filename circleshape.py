import pygame

from constants import SOUND_EFFECTS


class CircleShape(pygame.sprite.Sprite):
    """Base class for the shape of players and characters."""

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.name = None
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def _safe_color(self, c):
        try:
            return pygame.Color(c)
        except Exception:
            return pygame.Color("white")

    def out_of_bounds(self):
        w, h = pygame.display.get_surface().get_size()
        x, y, r = self.position.x, self.position.y, self.radius

        if x + r < 0 or x - r > w or y + r < 0 or y - r > h:
            return True
        return False

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        self.position += self.velocity * dt
        if self.out_of_bounds():
            self.kill()

    def respawn(self):
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
