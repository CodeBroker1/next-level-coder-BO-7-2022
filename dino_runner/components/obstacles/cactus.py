import random 
from dino_runner.components.obstacles.obstacle import Obstacles
## clase de herencia del obstaculo

class Cactus(Obstacles):

 def __init__ (self,image):
    self.type =random.randint(0,2)
    super().__init__(image,self.type)

    ## donde queremos que el cactus se muestre
    self.rect.y = 325

