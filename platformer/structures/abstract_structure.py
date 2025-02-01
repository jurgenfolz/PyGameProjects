import pygame

class Structure:
    def __init__(self, x, y, width, height, color=(100,100,100), texture=None):
        """
        :param x, y: Top-left position
        :param width, height: Dimensions
        :param color: (R,G,B)
        :param texture: Optional pygame.Surface for texture
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        # If you want a texture, load or assign it here
        # e.g. self.texture = pygame.image.load("platform.png")
        self.texture = texture
        if self.texture is not None:
            # Optionally scale the texture to match (width, height)
            self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        if self.texture:
            screen.blit(self.texture, (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, self.get_rect())

