import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        super().__init__(BIRD,self.type)
        self.rect.y=random.randint(100, 300)
        self.index=0

    def draw(self, SCREEEN):
        if self.index >= 9:
            self.index = 0
            
        SCREEEN.blit(self.image[self.index//5],self.rect)
        self.index += 1