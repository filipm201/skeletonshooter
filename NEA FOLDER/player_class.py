import pygame, sys
from random import randint, choice
import random
from projectile_class import Projectile
from obstacle_class import Obstacle
from enemy_class import Enemy
# from projectile_class import Projectile
pygame.init() #pygame module is initialised

#variables that need to be defined before main loop begins
clock = pygame.time.Clock() # clock variable can be used to easily measure time intervals

#screen management

# screen = pygame.display.set_mode((1920,1080)) #variable that defines the surface on which images and other surfaces will be drawn, and takes a tuple as an argument, in the form of (width, height)

class  Player(pygame.sprite.Sprite): # Player class is defined, and inherits from the pygame.sprite,Sprite class which comes from the pygame module
    def __init__(self, startingHealth, startingVelocity, projectileSpeed,
startingFirerate, startingDamage): # attributes of the player class are initialised in the constructor method
        super().__init__() #super method used to prevent any issues that may come from not using it
        self.image = pygame.image.load("C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/character.png") # self.image is a unique attribute and must be defined in a specific way, the pygame.sprite.Sprite is responsible for its unique behaviour
        self.rect = self.image.get_rect(center=(640,360)) # self.rect will be used to define and easily change the position of the player
        self.health = startingHealth
        self.velocity = startingVelocity
        self.reload = startingFirerate
        self.damage = startingDamage
        self.gunspeed = projectileSpeed
        self.playerDirection = pygame.math.Vector2() # creates a tuple (x, y) that can be used for directions
        self.timer=pygame.time.get_ticks()
        self.cooldown=False
        self.countticks=0

    def getxpos(self): # this function takes no parameters (not including self), and returns the players x-position
        return self.rect.center[0]

    def getypos(self): # this function takes no parameters (not including self), and returns the players y-position
        return self.rect.center[1]

    def playerMovement(self,obstgroup): # A procedure responsible for the players movement, using the WASD keys

        tempkey = pygame.key.get_pressed()

        holdvaluex=self.rect.centerx
        holdvaluey=self.rect.centery

        if tempkey[pygame.K_w]:
            self.playerDirection.y=-1
# if w key is pressed, direction is defined as negative (due to how pygame coordinates work) and a value is added to the y coordinate of the players position

        elif tempkey[pygame.K_s]:
                self.playerDirection.y=1
# opposite direction is chosen if s key is pressed, and added in same manner
        else:
            self.playerDirection.y=0 # direction is reset if there is no vertical movement key detected

        self.rect.centery+=self.playerDirection[1]*self.velocity

        if pygame.sprite.spritecollide(self,obstgroup,False,collided=None):
            self.rect.centery = holdvaluey
        if tempkey[pygame.K_a]:
            self.playerDirection.x=-1
 # same process for a and d keys. d is positive direction, a is negative direction

        elif tempkey[pygame.K_d]:
                self.playerDirection.x=1
        else:
            self.playerDirection.x=0 # direction is reset if there is no horizontal movement key detected

        self.rect.centerx+=self.playerDirection[0]*self.velocity

        if pygame.sprite.spritecollide(self,obstgroup,False,collided=None):
            self.rect.centerx = holdvaluex

    def playerShoot(self,group):

        key=pygame.key.get_pressed() # Temporary value, which is whatever key is detected to be pressed

        if self.cooldown == True:
            self.countticks+=1

        if self.countticks >= self.reload:
            self.cooldown = False
            self.countticks = 0

        if self.cooldown == False:
            if key[pygame.K_UP]:# Projectile is created, with a different direction depending on what key is pressed.
                group.add(Projectile(self.rect.centerx,self.rect.centery,'up'))
                self.cooldown = True

            if key[pygame.K_LEFT]:
                group.add(Projectile(self.rect.centerx,self.rect.centery,'left'))
                self.cooldown = True

            if key[pygame.K_DOWN]:
                group.add(Projectile(self.rect.centerx,self.rect.centery,'down'))
                self.cooldown = True

            if key[pygame.K_RIGHT]:
                group.add(Projectile(self.rect.centerx,self.rect.centery,'right'))
                self.cooldown = True

    def shootCooldown(self, cooldown):
        timetick = pygame.time.get_ticks()



    def takeDmg(self,enemygroup):
        if pygame.sprite.spritecollide(self,enemygroup,True,collided=None):
            self.health-=5

    def getpickedup(self,pickupgroup):
        if pygame.sprite.spritecollide(self,pickupgroup,True,collided=None):
            randomvalue = randint(0,4)
            if randomvalue == 0:
                self.health=round(self.health*1.1)
            elif randomvalue == 1:
                self.velocity=round(self.velocity*1.1)
            elif randomvalue == 2:
                self.reload=round(self.reload*0.9)
            elif randomvalue == 3:
                self.damage=round(self.damage*1.1)
            elif randomvalue == 4:
                self.gunspeed=round(self.gunspeed*1.1)

    def validmove(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 1280:
            self.rect.right = 1280

    def update(self,obstgroup,projgroup,pickupgroup,screen):
        self.playerMovement(obstgroup)
        self.validmove()
        self.playerShoot(projgroup)
        projgroup.update(self.gunspeed)
        projgroup.draw(screen)
        self.getpickedup(pickupgroup)

# while True: #Main game loop
#     screen.fill('black') #Background is given a colour, to draw over previous drawn player sprites
#     for event in pygame.event.get(): # iterates through what is returned from the pygame.event.get() function
#         if event.type==pygame.QUIT: # if the game is closed
#             pygame.quit()
#             sys.exit() # closes the game appropriately
#     obstGroup.draw(screen)
#     grpsngl.draw(screen) # plyr object is drawn on the screen
#     plyr.playerUpdate()
#     projectilegroup.draw(screen)
#     pygame.display.update() # display is updated
#     clock.tick(60) # constant frames per second is set to 60
