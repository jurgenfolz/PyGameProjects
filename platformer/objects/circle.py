from .abstract_object import Object
import pygame

class Circle(Object):
    def __init__(self, x, y, radius, color=(255,0,0), gravity=0.5):
        super().__init__(x - radius, y - radius, 2*radius, 2*radius, gravity)
        self.radius = radius
        self.color = color

        self.move_speed = 5
        self.jump_speed = 12

    def draw(self, screen):
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
        # Only jump if on_ground is True
        if self.on_ground:
            self.y_vel = -self.jump_speed
            # Once we jump, we can set on_ground = False if desired
            self.on_ground = False
