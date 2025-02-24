import pygame 

class Oscillator: 
    def __init__(self, equilibrium_pos, spring_constant, block_mass): 
        self.equilibrium_pos = equilibrium_pos 
        self.k = spring_constant 
        self.m = block_mass


    def draw(self, screen): 
        pygame.draw.rect(screen, (255,0,0),(100,100,100,100),0)

    def move(self): 
        pass 




