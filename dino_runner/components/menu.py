import pygame
import pygame.font
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.utils.constants import COLOR

class Menu :
 def __init__(self):
    pygame.font.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.font1 = pygame.font.Font(None, 50)
    self.font2 = pygame.font.Font(None, 30)   
    self.text_start = self.font1.render("Press any Key to Start", True, (0, 0, 0))
    self.text_startRect= self.text_start.get_rect ()
    self.text_startRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
   # pygame.quit() 
   # pygame.display.update()
   # pygame.display.flip()   

 def inicial (self):
     self.screen.fill(COLOR)
     self.screen.blit(self.text_start, self.text_startRect)
     pygame.display.update()
     pygame.display.flip()  


