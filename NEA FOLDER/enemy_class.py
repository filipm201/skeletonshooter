import pygame, sys, math
from random import randint, choice
import random
pygame.init() #pygame module is initialised

from pickup_class import Pickup

#variables that need to be defined before main loop begins
# clock = pygame.time.Clock() # clock variable can be used to easily measure time intervals

#screen management

# screen = pygame.display.set_mode((1280,720)) #variable that defines the surface on which images and other surfaces will be drawn, and takes a tuple as an argument, in the form of (width, height)

#class  Player(pygame.sprite.Sprite): # Player class is defined, and inherits from the pygame.sprite,Sprite class which comes from the pygame module
#     def __init__(self, startingHealth, startingVelocityx, startingVelocityy, projectileSpeed,
# startingFirerate, startingDamage, playerImage): # attributes of the player class are initialised in the constructor method
#         super().__init__() #super method used to prevent any issues that may come from not using it
#         self.image = pygame.image.load(playerImage) # self.image is a unique attribute and must be defined in a specific way, the pygame.sprite.Sprite is responsible for its unique behaviour
#         self.rect = self.image.get_rect(center=(640,360)) # self.rect will be used to define and easily change the position of the player
#         self.health = startingHealth
#         self.velocityx = startingVelocityx
#         self.velocityy = startingVelocityy
#         self.reload = startingFirerate
#         self.damage = startingDamage
#         self.gunspeed = projectileSpeed
#         self.playerDirection = pygame.math.Vector2() # creates a tuple (x, y) that can be used for directions

#     def playerMovement(self): # A procedure responsible for the players movement, using the WASD keys
#         tempkey = pygame.key.get_pressed()
#         if tempkey[pygame.K_w]:
#             self.playerDirection.y=-1
#             self.rect.center+=self.playerDirection*self.velocityy # if w key is pressed, direction is defined as negative (due to how pygame coordinates work) and a value is added to the y coordinate of the players position
#         elif tempkey[pygame.K_s]:
#             self.playerDirection.y=1
#             self.rect.center+=self.playerDirection*self.velocityy # opposite direction is chosen if s key is pressed, and added in same manner
#         else:
#             self.playerDirection.y=0 # direction is reset if there is no vertical movement key detected

#         if tempkey[pygame.K_a]:
#             self.playerDirection.x=-1
#             self.rect.center+=self.playerDirection*self.velocityx # same process for a and d keys. d is positive direction, a is negative direction
#         elif tempkey[pygame.K_d]:
#             self.playerDirection.x=1
#             self.rect.center+=self.playerDirection*self.velocityx
#         else:
#             self.playerDirection.x=0 # direction is reset if there is no horizontal movement key detected
#     def getxpos(self): # this function takes no parameters (not including self), and returns the players x-position
#         return self.rect.center[0]

#     def getypos(self): # this function takes no parameters (not including self), and returns the players y-position
#         return self.rect.center[1]

class Enemy(pygame.sprite.Sprite):
    def __init__(self,givenVelocityx,givenVelocityy):
        super().__init__()

        self.velocityx=givenVelocityx
        self.velocityy=givenVelocityy
        self.image=pygame.image.load("C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/skeleton front view.png")
        self.rect=self.image.get_rect(center=(randint(0,1280),randint(0,720)))
        self.health = 15
        self.result=0
        
    def enemyBehaviour(self,plyrobject): # This method will decide where the enemy moves, based on the players position.
        if self.rect.x > plyrobject.getxpos():
            self.rect.x-=self.velocityx # if the x position is larger than the players, it will lessen the x-position so that the enemy moves closer to the player
        elif self.rect.x == plyrobject.getxpos():
            pass # if the x position is the same as the players, it will not adjust as it is already as close as it can be to the players x position
        else:
            self.rect.x+=self.velocityx # the only other scenario left is that the x-position is lesser than the players, so this will increase it to move closer to the player
    
        if self.rect.y > plyrobject.getypos(): # same adjustments are applied, but to the y-positions
            self.rect.y-=self.velocityy
        elif self.rect.y == plyrobject.getypos():
            pass
        else:
            self.rect.y+=self.velocityy

    def takeDamage(self,projgroup,pickupgroup,damagenum):

        if pygame.sprite.spritecollide(self,projgroup,True,collided=None): # DOESNT WORK, AS RANDOM ENEMIES TAKE DAMAGE. DO LIST AND SEE IF SELF IS IN IT.
            self.health-=damagenum # If a projectile shot by the player collides with the enemy, they will take damage

        if self.health<=0:
            if randint(0,1):# random chance to spawn a pickup, as code will only run if 1 is returned. This is because 1 is the equivalent to the boolean value of True.
                currentpos = self.rect.center
                pickupgroup.add(Pickup(currentpos)) # A new pickup object is created in the position of death
            self.result=1
            pygame.sprite.Sprite.kill(self) #The enemy object sprite is removed from the enemygroup
        
        return self.result

    def update(self,plyrobject):
        self.enemyBehaviour(plyrobject)
        # print(self.takeDamage(projgroup,pickupgroup,damagenum))

    



# enemygroup = pygame.sprite.Group()

# plyr=Player(1,1.28,0.72,5,5,5,"C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/skeleton character frames.png") # object with placeholder arguments is created for testing purposes
# grpsngl=pygame.sprite.GroupSingle() #group is created to hold a single sprite. in this case, plyr so that it can be easily drawn
# grpsngl.add(plyr) # plyr object is added to the group

# def grabplayerpos(obj,xory = str):
#     return obj.get(xory)

# while True: #Main game loop

#     screen.fill('black') #Background is given a colour, to draw over previous drawn player sprites
#     for event in pygame.event.get(): # iterates through what is returned from the pygame.event.get() function
#         if event.type==pygame.QUIT: # if the game is closed
#             pygame.quit()
#             sys.exit() # closes the game appropriately
        
#         if event.type==ENEMYSPWN:
#             tempenemy = Enemy(randint(0,1000),randint(0,1000),1,1)
#             enemygroup.add(tempenemy)

#     grpsngl.draw(screen) # plyr object is drawn on the screen
    
#     plyr.playerMovement() # plyr movement procedure is called, moving the player depending on the input
#     for x in enemygroup:
#         x.enemyBehaviour()
#     enemygroup.draw(screen)
#     pygame.display.update() # display is updated
#     clock.tick(60) # constant frames per second is set to 60
