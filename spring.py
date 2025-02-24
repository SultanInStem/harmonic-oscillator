import math
import pygame
from globals import to_math, to_screen
class Spring: 
    def __init__(self, amp, t, spring_constant, start_pos, end_pos):
        self.amp = amp 
        self.k = spring_constant
        self.t = t
        self.start_pos = start_pos 
        self.end_pos = end_pos 
        # self.length_range = int(math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2))


    def draw(self, screen):
        for i in range(0, 100):

            pygame.draw.circle(screen, (255,255,255), to_screen((i, 1000*math.sin(self.t * i))), 1, 0)


     