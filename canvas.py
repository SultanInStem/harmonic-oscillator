import pygame 
import sys 
from config import SCREEN_SIZE
from globals import to_screen, to_math
from oscillator import Oscillator

class Canvas: 
    def __init__(self): 
        pygame.init()
        self.running = True
        self.dragging = False 
        self.fps = 60
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Simple Harmonic Oscillator")

        self.clock = pygame.time.Clock()
        self.dt = 1 / self.fps
        self.t = 0 

        mass = float(input("Enter the mass of the block: ")) 
        spring_constant = float(input("Enter the spring constant: "))



        self.block_coordinate_origin = (-500,-200)
        self.oscillator = Oscillator((0,0), spring_constant, mass, self.block_coordinate_origin, (75,75))


    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.oscillator.is_clicked(event.pos): 
                self.dragging = True
                self.t = 0
            elif event.type == pygame.MOUSEBUTTONUP: 
                self.dragging = False 
            elif event.type == pygame.MOUSEMOTION and self.dragging: 
                self.oscillator.set_pos(event.pos)

    def update(self):
        if self.dragging == False: 
            self.t += self.dt
            self.oscillator.move(self.t) 
    def render(self): 
        self.screen.fill((0,0,0))

        self.oscillator.draw(self.screen)

        ### Drawing coordinate for the block-spring system 
        pygame.draw.circle(
            self.screen, 
            (255,0,0), 
            to_screen((0,0)),
            4,
            0
        )
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