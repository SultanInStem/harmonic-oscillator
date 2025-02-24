import pygame 
import sys 
from config import SCREEN_SIZE
from globals import to_screen, to_math
from oscillator import Oscillator
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Simple Harmonic Oscillator")

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.block_coordinate_origin = (-500,-200)

        self.oscillator = Oscillator((0,0), 20, 1, self.block_coordinate_origin, (100,100))

    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def update(self):
        self.oscillator.move() 
    def render(self): 
        self.screen.fill((0,0,0))

        self.oscillator.draw(self.screen)

        ### Drawing coordinate for the block-spring system 
        pygame.draw.line(
            self.screen, 
            (255,255,255), 
            to_screen(self.block_coordinate_origin), 
            to_screen((self.block_coordinate_origin[0], 50)), 
            1
        )
        pygame.draw.line(
            self.screen, 
            (255,255,255), 
            to_screen(self.block_coordinate_origin), 
            to_screen((600,self.block_coordinate_origin[1])), 
            1
        )


        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()