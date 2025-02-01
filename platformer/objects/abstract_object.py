import pygame
class Object:
    def __init__(self, x, y, width, height, gravity=0.5):
        """
        :param x, y: Position (top-left for bounding box)
        :param width, height: Dimensions for bounding box
        :param gravity: Amount of gravitational acceleration
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Velocity
        self.x_vel = 0
        self.y_vel = 0

        # Physical properties
        self.gravity = gravity

    def get_rect(self):
        """Return a pygame.Rect for collision checks."""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, structures):
        """
        Axis-by-axis movement:
          1) Add gravity to y_vel
          2) Move horizontally, check collision
          3) Move vertically, check collision
        """
        # Apply gravity each frame
        self.y_vel += self.gravity

        # 1) Move horizontally
        self.x += self.x_vel
        self.resolve_collisions_x(structures)

        # 2) Move vertically
        self.y += self.y_vel
        self.resolve_collisions_y(structures)

    def resolve_collisions_x(self, structures):
        """Correct horizontal overlap with any structure."""
        rect = self.get_rect()
        for struct in structures:
            if rect.colliderect(struct.get_rect()):
                # Moving right
                if self.x_vel > 0:
                    self.x = struct.get_rect().left - self.width
                # Moving left
                elif self.x_vel < 0:
                    self.x = struct.get_rect().right
                # Zero out horizontal velocity upon collision
                self.x_vel = 0
                rect = self.get_rect()  # Update rect after reposition

    def resolve_collisions_y(self, structures):
        """Correct vertical overlap with any structure."""
        rect = self.get_rect()
        for struct in structures:
            if rect.colliderect(struct.get_rect()):
                # Moving down
                if self.y_vel > 0:
                    self.y = struct.get_rect().top - self.height
                # Moving up
                elif self.y_vel < 0:
                    self.y = struct.get_rect().bottom
                # Zero out vertical velocity upon collision
                self.y_vel = 0
                rect = self.get_rect()  # Update rect after reposition

    def draw(self, screen):
        """Base class doesn't implement drawing. Subclasses should override."""
        pass
