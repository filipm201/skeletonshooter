# file path for images is: C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER
import pygame, sys # player_class, enemy_class, obstacle_class, projectile_class
from random import randint, choice
pygame.init()

#variables
clock = pygame.time.Clock()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, randPosx, randPosy): # when an obstacle object is created, it will take 2 parameters for where its position will be. This is the only thing that will differ-
        #- between obstacle objects, everything else will be standardised.
        super().__init__()
        self.image=pygame.image.load('C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/basic environment obstacles.png')
        self.rect=self.image.get_rect(center=(randPosx,randPosy)) # It will be placed in the parameters given
# obstGroup = pygame.sprite.Group()

# obstGroup.add(Obstacle(randint(0,1920), randint(0,1080)) for x in range(0,40)) # A comprehension to generate a list of 40 randomly placed obstacles. 

##This uses much less lines of code, than if i were to use a for loop and append a list using it. This, will make the program run more efficiently.

#screen management

# screen = pygame.display.set_mode((1920,1080))

# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     obstGroup.draw(screen)
#     pygame.display.update()
#     clock.tick(60)