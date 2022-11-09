import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        #random = REACT.Y (250,200)
        self.obstacle_type = 0
        super().__init__(image,self.obstacle_type)
        self.rect.y=random.randint(100, 300)
        self.index=0

    def draw(self, SCREEEN):
        if self.index >= 9:
            self.index = 0
        SCREEEN.blit(self.image[self.index//5],self.rect)
        self.index += 1