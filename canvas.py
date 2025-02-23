import pygame 
import sys 
from config import SCREEN_SIZE
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Simple Harmonic Oscillator")

        self.clock = pygame.time.Clock()
        self.fps = 60

    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def update(self): 
        pass 
    def render(self): 
        self.screen.fill((0,0,0))

        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()