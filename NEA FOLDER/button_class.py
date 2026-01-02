# file path for images is: C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER
import pygame, sys, player_class, enemy_class, obstacle_class, projectile_class
from random import randint, choice
pygame.init()

class button(pygame.sprite.Sprite):
    def __init__(self,givenxpos,givenypos,widthheight,colour,textonbutton):
        super().__init__()
        #whatever text will be in it, what colour and then combined into one.
        fontused=pygame.font.SysFont('Calibri',10,False,False)

        self.image = fontused.render(str(textonbutton),True,'Black',widthheight)
        self.rect = pygame.image.get_rect(center=(givenxpos,givenypos))
        self.image.fill(colour)
        


