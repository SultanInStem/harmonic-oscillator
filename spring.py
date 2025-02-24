import math
import pygame
from globals import to_math, to_screen
class Spring: 
    def __init__(self, amp, wave_num, spring_constant, start_pos, end_pos):
        self.amp = amp 
        self.k = spring_constant
        self.wave_num = wave_num 
        self.start_pos = start_pos 
        self.end_pos = end_pos 

    def draw(self, screen):
        length = self.k * math.pi / self.wave_num
        t = 0 
        while(t < length*500): 
            t += 0.1 
            x = self.start_pos[0] + t  
            y = self.amp * math.sin(self.wave_num * x)
            pygame.draw.circle(screen, (0,200,50), to_screen((x,y)), 1, 0)

    def update(self): 
        pass