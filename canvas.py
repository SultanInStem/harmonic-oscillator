import pygame 
import sys 
from config import SCREEN_SIZE
from globals import to_screen, to_math, GREEN_COLOR
from oscillator import Oscillator
import math 

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
        
        mass = 10 
        spring_constant = 40

        # user_choice = input("Do you want to configure the simulation? y-yes or n-no ")
        # if user_choice.lower() == "y": 
        #     mass = float(input("Enter the mass of the block: ")) 
        #     spring_constant = float(input("Enter the spring constant: "))

        

        self.block_coordinate_origin = (-650,-200)
        self.coordinate_length = 420
        self.block_equilibrium_pos = (-100,0)
        self.oscillator = Oscillator((-100,0), spring_constant, mass, self.block_coordinate_origin, 75)

    def reset(self): 
        self.oscillator.set_pos(self.block_equilibrium_pos)
        self.oscillator.set_amp(0)
        self.t = 0
    def draw_spring(self): 
        n = 4 # number of crests 
        amp = 50 # amplitude 
        spacing = 5 # horizontal distance between plotted points
        start = self.block_coordinate_origin 
        end = self.oscillator.get_math_pos()
        d = end[0] - start[0]
        if d <= 0: return 
        



    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.oscillator.is_clicked(event.pos): 
                self.dragging = True
                self.t = 0
            elif event.type == pygame.MOUSEBUTTONUP: 
                self.dragging = False 
            elif event.type == pygame.MOUSEMOTION and self.dragging and to_math(event.pos)[0] >= self.block_coordinate_origin[0] and to_math(event.pos)[0] <= self.coordinate_length - self.oscillator.get_size(): 
                self.oscillator.set_pos(event.pos)
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_r: 
                    self.reset()
                

    def update(self):
        if self.dragging == False: 
            self.t += self.dt
            self.oscillator.move(self.t) 
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
            to_screen((self.coordinate_length,self.block_coordinate_origin[1])), 
            1
        )
        pygame.draw.line(
            self.screen, 
            GREEN_COLOR, 
            to_screen((self.block_equilibrium_pos[0],-250)), 
            to_screen((self.block_equilibrium_pos[0],-150)),
            2
        )
        ### Draw a spring
    


        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()