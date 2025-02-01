import pygame
import sys

class Circle:
    """
    A circle that can move left/right and jump under gravity.
    """

    def __init__(self, x, y, radius, color,
                 speed=5, jump_speed=15, gravity=0.5):
        """
        :param x: Initial x-position
        :param y: Initial y-position
        :param radius: Circle radius
        :param color: (R, G, B) color
        :param speed: Horizontal speed when moving left or right
        :param jump_speed: Initial vertical velocity when jumping
        :param gravity: Constant gravitational acceleration
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
        # Movement parameters
        self.speed = speed
        self.jump_speed = jump_speed
        self.gravity = gravity
        
        # Current velocities
        self.x_vel = 0
        self.y_vel = 0

    def update(self, screen_width, screen_height):
        """
        Apply gravity, update position, and handle ground/ceiling collision.
        """
        # Apply gravity
        self.y_vel += self.gravity
        
        # Update positions
        self.x += self.x_vel
        self.y += self.y_vel
        
        # Stop at the left edge
        if self.x - self.radius < 0:
            self.x = self.radius
        
        # Stop at the right edge
        if self.x + self.radius > screen_width:
            self.x = screen_width - self.radius
        
        # Stop at the top edge (optional: we can let the circle just go off-screen if you want)
        if self.y - self.radius < 0:
            self.y = self.radius
            self.y_vel = 0
        
        # Land on the bottom (ground)
        if self.y + self.radius > screen_height:
            self.y = screen_height - self.radius
            self.y_vel = 0

    def draw(self, surface):
        """
        Draw the circle on the given surface.
        """
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
    
    def is_on_ground(self, screen_height):
        """
        Check if the circle is on (or very close to) the bottom of the screen.
        """
        return abs((self.y + self.radius) - screen_height) < 1
    
    def move_left(self):
        self.x_vel = -self.speed
    
    def move_right(self):
        self.x_vel = self.speed
    
    def stop_horizontal_movement(self):
        self.x_vel = 0
    
    def jump(self):
        """
        Set an upward velocity if on the ground.
        """
        self.y_vel = -self.jump_speed


class Game:
    """
    Main game class handling initialization, the main loop, user input, and cleanup.
    """

    def __init__(self, width=800, height=600, fps=60):
        pygame.init()
        
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Move and Jump with Gravity")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Background color
        self.bg_color = (30, 30, 30)
        
        # Create a circle object
        self.circle = Circle(
            x=self.width // 2,
            y=self.height // 2,
            radius=30,
            color=(255, 0, 0),
            speed=5,
            jump_speed=15,
            gravity=0.5
        )
    
    def run(self):
        """
        Run the main game loop.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        self.quit()
    
    def handle_events(self):
        """
        Handle all incoming events, including key presses for movement.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        # Continuous keyboard state
        keys = pygame.key.get_pressed()
        
        # Left/right movement
        if keys[pygame.K_LEFT]:
            self.circle.move_left()
        elif keys[pygame.K_RIGHT]:
            self.circle.move_right()
        else:
            self.circle.stop_horizontal_movement()
        
        # Jumping
        if keys[pygame.K_SPACE]:
            # Only jump if on the ground
            if self.circle.is_on_ground(self.height):
                self.circle.jump()

    def update(self):
        """
        Update the game state.
        """
        self.circle.update(self.width, self.height)

    def draw(self):
        """
        Draw everything to the screen.
        """
        self.screen.fill(self.bg_color)
        self.circle.draw(self.screen)
        pygame.display.flip()

    def quit(self):
        """
        Clean up and close the game.
        """
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
