import pygame, sys # player_class, enemy_class, obstacle_class, projectile_class
from random import randint, choice
pygame.init()

class Pickup(pygame.sprite.Sprite):

    def __init__(self,givenpos):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill((randint(0,100),randint(0,100),randint(0,100)))
        self.rect = self.image.get_rect(center=(givenpos))
