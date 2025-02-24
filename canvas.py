import pygame 
import sys 
from config import SCREEN_SIZE
from globals import to_screen, to_math
from oscillator import Oscillator
from spring import Spring 
import math
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.PI = 3.14
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Simple Harmonic Oscillator")

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.block_coordinate_origin = (-500,-200)

        self.oscillator = Oscillator((0,0), 20, 1, self.block_coordinate_origin, (100,100))

        self.spring = Spring(10, math.pi * 2, 5, (0,0), (100,0))
        self.t = 20

    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def update(self):
        self.oscillator.move() 
    def render(self): 
        self.screen.fill((0,0,0))

        self.oscillator.draw(self.screen)

        x = 0
        A = 100
        while (x < 400): 
            x += 1
            y = A * math.sin(self.t*self.PI*x)
            pygame.draw.circle(self.screen, (255,255,255), to_screen((x,y)), 2,0)
        self.t += 0.00001

        if self.t >= 40: 
            self.t = 20

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