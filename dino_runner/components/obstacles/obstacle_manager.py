from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle_bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacles2=[]
        self.obstacles3=[]

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

        if len(self.obstacles) == 0:
            if random.randint(0,2)== 0:
                cactus2 = Cactus(LARGE_CACTUS)
                self.obstacles.append(cactus2)
                

        for obstacle in self.obstacles2:
            obstacle.update(game.game_speed, self.obstacles2)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break
        
        if len(self.obstacles)==0:
            bird = Bird(BIRD)
            self.obstacles.append(bird)
        
        for obstacle in self.obstacles3:
            obstacle.update(game.game_speed, self.obstacles3)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break
        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)