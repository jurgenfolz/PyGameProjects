import pygame

class Object:
    def __init__(self, x, y, width, height, gravity=0.5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.x_vel = 0
        self.y_vel = 0
        self.gravity = gravity

        # Track whether this object is on the ground (or on top of any structure)
        self.on_ground = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, structures):
        """
        Axis-by-axis movement:
        1) Add gravity to y_vel
        2) Move horizontally, check collision
        3) Move vertically, check collision
        """
        # Clear on_ground flag each frame, will set it again if we land
        self.on_ground = False

        # 1) Gravity
        self.y_vel += self.gravity

        # 2) Move horizontally
        self.x += self.x_vel
        self.resolve_collisions_x(structures)

        # 3) Move vertically
        self.y += self.y_vel
        self.resolve_collisions_y(structures)

    def resolve_collisions_x(self, structures):
        rect = self.get_rect()
        for struct in structures:
            if rect.colliderect(struct.get_rect()):
                # Moving right
                if self.x_vel > 0:
                    self.x = struct.get_rect().left - self.width
                # Moving left
                elif self.x_vel < 0:
                    self.x = struct.get_rect().right
                self.x_vel = 0
                rect = self.get_rect()  # update bounding box

    def resolve_collisions_y(self, structures):
        rect = self.get_rect()
        for struct in structures:
            if rect.colliderect(struct.get_rect()):
                # Moving down (from above)
                if self.y_vel > 0:
                    self.y = struct.get_rect().top - self.height
                    self.y_vel = 0
                    self.on_ground = True  # Landed on a structure
                # Moving up (hit the ceiling)
                elif self.y_vel < 0:
                    self.y = struct.get_rect().bottom
                    self.y_vel = 0
                rect = self.get_rect()  # update bounding box

    def draw(self, screen):
        pass
