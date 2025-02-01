from .abstract_object import Object
import pygame

class Circle(Object):
    def __init__(self, x, y, radius, color=(255,0,0), gravity=0.5):
        """
        Circle is still a bounding box for collisions, but we store radius
        for drawing. The bounding box is (2*radius x 2*radius).
        """
        super().__init__(x - radius, y - radius, 2*radius, 2*radius, gravity)
        self.radius = radius
        self.color = color

        # Movement attributes
        self.move_speed = 5
        self.jump_speed = 12

    def draw(self, screen):
        # Draw a circle centered on (self.x + radius, self.y + radius)
        center_x = int(self.x + self.radius)
        center_y = int(self.y + self.radius)
        pygame.draw.circle(screen, self.color, (center_x, center_y), self.radius)

    def move_left(self):
        self.x_vel = -self.move_speed

    def move_right(self):
        self.x_vel = self.move_speed

    def stop_horizontal(self):
        self.x_vel = 0

    def jump(self):
        # Only jump if velocity is ~0 in y-direction (on ground)
        # In a more robust system, you'd check collisions or ground contact
        if abs(self.y_vel) < 0.01:
            self.y_vel = -self.jump_speed

