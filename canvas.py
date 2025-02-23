import pygame 
import sys 

class Canvas: 
    def __init__(self): 
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode()

    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False
    def update(self): 
        pass 
    def render(self): 



        pygame.display.flip()

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()