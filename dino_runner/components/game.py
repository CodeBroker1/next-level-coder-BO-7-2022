import pygame
import pygame.font
import pygame.event
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, COLOR, COLOR2, COLOR3
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import Obstaclemanager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.extras.extras_manager import ExtrasManager
from dino_runner.components.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.player = Dinosaur()
        self.obstacle_manager = Obstaclemanager()
        self.power_up_manager= PowerUpManager()
        self.menu = Menu()
        self.extras = ExtrasManager()
        self.font = pygame.font.Font(None,30)
        self.font2 = pygame.font.Font(None,30)

    def score (self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1
        self.text = self.font.render('Points '+ str(self.points),True,(0,0,0))
        self.textRect= self.text.get_rect()
        self.textRect.center = (1000,40) 
        self.screen.blit (self.text, self.textRect)

    def square (self):
        pygame.draw.rect(self.screen,(COLOR3),(940,20,125,43))

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update (self.game_speed,self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.extras.update(self.game_speed)
        self.player.check_invincibility()
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(COLOR)
        self.halfscreen ()
        self.draw_background()
        self.square()
        self.score()
        self.player.draw (self.screen)
        self.obstacle_manager.draw (self.screen)
        self.power_up_manager.draw(self.screen)
        self.extras.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def halfscreen (self):
        self.screen.fill(COLOR2,(0, 385, 1100, 1000))

    def draw_background(self):
        self.score ()
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG,(image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

        
                        
                   
