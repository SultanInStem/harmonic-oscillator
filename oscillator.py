import pygame 
from globals import to_screen, to_math
import math
class Oscillator: 
    def __init__(self, equilibrium_pos, spring_constant, block_mass, origin, size): 
        self.equilibrium_pos = equilibrium_pos 
        self.k = spring_constant 
        self.m = block_mass
        self.origin = origin
        self.block_size = size 
        self.pos = (equilibrium_pos[0], origin[1] + self.block_size[1])


    def draw(self, screen): 
        ### Drawing the block 
        screen_x = to_screen(self.pos)[0]
        screen_y = to_screen(self.pos)[1]
        pygame.draw.rect(screen, (255,0,0),(screen_x, screen_y, self.block_size[0], self.block_size[1]), 0)
        

        ### Drawing the spring 

    def move(self): 
        pass 




