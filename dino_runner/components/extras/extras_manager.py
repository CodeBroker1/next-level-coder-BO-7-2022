
from dino_runner.components.extras.cloud import Cloud
from dino_runner.utils.constants import CLOUD


class ExtrasManager:
    def __init__(self):
        self.extras = []

    def update (self,game_speed):
     if len (self.extras) == 0:
           self.extras.append(Cloud(CLOUD))

     for extra in self.extras:
        extra.update (game_speed,self.extras)    

    def draw(self,screen):
        for extra in self.extras:
            extra.draw(screen)