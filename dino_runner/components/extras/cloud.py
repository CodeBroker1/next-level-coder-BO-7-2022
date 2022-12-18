from dino_runner.components.extras.extra import Extras

class Cloud(Extras):

 def __init__ (self,image):
    self.image = image
    
    super().__init__(image,0)