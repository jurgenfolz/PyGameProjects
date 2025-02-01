import pygame
import sys
from objects.circle import Circle
from structures.abstract_structure import Structure
from structures.ground import Ground


class Game:
    def __init__(self, width=800, height=600, fps=60):
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("OOP Example: Objects, Structures, Ground")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Create our Circle (the player)
        self.player = Circle(x=self.width//2, y=100, radius=25, color=(0,255,0), gravity=0.5)
        
        # Create some structures
        self.structures = []
        
        # A small platform in the middle
        platform = Structure(x=300, y=400, width=200, height=20, color=(150,100,50))
        self.structures.append(platform)
        
        # Ground at the bottom
        ground = Ground(x=0, y=self.height-40, width=self.width, height=40, color=(120,60,0))
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
        # Update the player (which checks collisions against structures)
        self.player.update(self.structures)

    def draw(self):
        self.screen.fill((30, 30, 30))
        
        # Draw structures
        for struct in self.structures:
            struct.draw(self.screen)
        
        # Draw player
        self.player.draw(self.screen)
        
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
