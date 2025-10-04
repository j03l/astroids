import pygame


class Interface(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.font_path = "font/start-2p.ttf"
        self.font_size = 35
        self.color = "white"
        self.text = "Test"

    def center_of_word(self, font):
        x, y = font.size(self.text)
        return self.x - (x / 2), self.y - (y / 2)

    def update(self):
        pass

    def draw(self, screen):
        font = pygame.font.Font(self.font_path, self.font_size)
        screen.blit(font.render(self.text, True, self.color), self.center_of_word(font))
