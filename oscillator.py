import pygame 
from globals import to_screen, to_math
import math

class Oscillator: 
    def __init__(self, equilibrium_pos, spring_constant, block_mass, origin, size): 
        self.equilibrium_pos = equilibrium_pos 
        self.spring_const = spring_constant 
        self.m = block_mass
        self.origin = origin
        self.size = size 
        self.pos = (equilibrium_pos[0], origin[1] + size)
        self.omega = math.sqrt(spring_constant / block_mass)
        self.amplitude = 0
    def set_amp(self, a):
        self.amplitude = a
    def draw(self, screen): 
        ### Drawing the block 
        screen_x = to_screen(self.pos)[0]
        screen_y = to_screen(self.pos)[1]
        pygame.draw.rect(screen, (255,0,0),(screen_x, screen_y, self.size, self.size), 0)

    def move(self, t): 
        x = self.amplitude * math.cos(self.omega * t) + self.equilibrium_pos[0]
        self.pos = (x, self.pos[1])

    def set_pos(self, point):
        p = to_math(point)
        self.pos = (p[0], self.origin[1] + self.size) 
        self.amplitude = p[0] - self.equilibrium_pos[0]
    
    def is_clicked(self, point): 
        p = to_math(point)
        pos = self.pos 
        if p[0] >= pos[0] and p[0] <= pos[0] + self.size and p[1] <= pos[1] and p[1] >= pos[1] - self.size:
            return True
        return False 
    def get_math_pos(self): 
        return self.pos 
    def get_size(self): 
        return self.size






