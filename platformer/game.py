import pygame
import sys
from .objects.circle import Circle
from .structures.abstract_structure import Structure
from .structures.ground import Ground
from .camera.camera import Camera 

class Game:
    def __init__(self, width=800, height=600, fps=60):
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("OOP Example: Objects, Structures, Ground")

        # Suppose your entire world is 2400 wide x 800 high
        self.world_width = 2400
        self.world_height = 800

        self.camera = Camera(
            screen_width=self.width,
            screen_height=self.height,
            world_width=self.world_width,
            world_height=self.world_height
        )
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Create our Circle (the player)
        self.player = Circle(x=self.width//2, y=100, radius=25, color=(0,255,0), gravity=0.5)
        
        self.structures = []

        # Existing platform at x=300, y=400
        platform1 = Structure(300, 400, 200, 20, color=(150,100,50))
        self.structures.append(platform1)

        # Another platform far off to the right
        platform2 = Structure(1200, 350, 200, 20, color=(150,50,150))
        self.structures.append(platform2)

        # Another one up high
        platform3 = Structure(500, 200, 100, 20, color=(255,255,0))
        self.structures.append(platform3)

        # Ground at bottom
        ground = Ground(0, self.height-40, width=self.width*3, height=40, color=(120,60,0))
        # width=self.width*3 => ground is 2400 px wide, for example
        self.structures.append(ground)


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        self.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        keys = pygame.key.get_pressed()
        # Left / Right
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        else:
            self.player.stop_horizontal()

        # Jump
        if keys[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        # Update player logic (movement, collisions)
        self.player.update(self.structures)

        # Update the camera to follow the player's center
        player_center_x = self.player.x + self.player.width // 2
        player_center_y = self.player.y + self.player.height // 2
        self.camera.update(player_center_x, player_center_y)

    def draw(self):
        self.screen.fill((30, 30, 30))

        # Draw structures
        for struct in self.structures:
            # Convert structure's world coords to screen coords
            draw_x, draw_y = self.camera.apply(struct.x, struct.y)
            # We can either:
            # 1) Make a copy of struct's rect and offset it, OR
            # 2) Just shift the x,y before drawing

            if struct.texture:
                # We might do:
                self.screen.blit(struct.texture, (draw_x, draw_y))
            else:
                rect = pygame.Rect(draw_x, draw_y, struct.width, struct.height)
                pygame.draw.rect(self.screen, struct.color, rect)

        # Draw player (circle)
        px, py = self.camera.apply(self.player.x, self.player.y)
        center_x = int(px + self.player.radius)
        center_y = int(py + self.player.radius)
        pygame.draw.circle(self.screen, self.player.color, (center_x, center_y), self.player.radius)

        pygame.display.flip()


    def quit(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
