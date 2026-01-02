import pygame, sys, math
from random import randint, choice
pygame.init() #pygame module is initialised

# #variables that need to be defined before main loop begins
# clock = pygame.time.Clock() # clock variable can be used to easily measure time intervals

# #screen management
# helddown=False
# screen = pygame.display.set_mode((1280,720)) #variable that defines the surface on which images and other surfaces will be drawn, and takes a tuple as an argument, in the form of (width, height)

# class  Player(pygame.sprite.Sprite): # Player class is defined, and inherits from the pygame.sprite,Sprite class which comes from the pygame module
#     def __init__(self, startingHealth, startingVelocity, projectileSpeed,
# startingFirerate, startingDamage, playerImage): # attributes of the player class are initialised in the constructor method
#         super().__init__() #super method used to prevent any issues that may come from not using it
#         self.image = pygame.image.load(playerImage) # self.image is a unique attribute and must be defined in a specific way, the pygame.sprite.Sprite is responsible for its unique behaviour
#         self.rect = self.image.get_rect(center=(640,360)) # self.rect will be used to define and easily change the position of the player
#         self.health = startingHealth
#         self.velocity = startingVelocity
#         self.reload = startingFirerate
#         self.damage = startingDamage
#         self.gunspeed = projectileSpeed
#         self.playerDirection = pygame.math.Vector2() # creates a tuple (x, y) that can be used for directions

#     def playerMovement(self): # A procedure responsible for the players movement, using the WASD keys

#         tempkey = pygame.key.get_pressed()


#         if tempkey[pygame.K_w]: # if w key is pressed, direction is defined as negative (due to how pygame coordinates work) and a value is added to the y coordinate of the players position
#             self.playerDirection.y=-1

#         elif tempkey[pygame.K_s]:
#             self.playerDirection.y=1

#         else:
#             self.playerDirection.y=0

#         if tempkey[pygame.K_a]:
#             self.playerDirection.x=-1

#         elif tempkey[pygame.K_d]:
#             self.playerDirection.x=1

#         else:
#             self.playerDirection.x=0

#         self.rect.center+=self.playerDirection*self.velocity



    # def playerShoot(self):
    #     key=pygame.key.get_pressed()



    #     if key[pygame.K_UP]:
    #         newproj = Projectile(5,5,'up')
    #         projectilegroup.add(newproj)


    #     if key[pygame.K_LEFT]:
    #         newproj = Projectile(5,5,'left')
    #         projectilegroup.add(newproj)


    #     if key[pygame.K_DOWN]:
    #         newproj = Projectile(5,5,'down')
    #         projectilegroup.add(newproj)


    #     if key[pygame.K_RIGHT]:
    #         newproj = Projectile(5,5,'right')
    #         projectilegroup.add(newproj)

#     def playerUpdate(self):
#         timetake=pygame.time.get_ticks()
#         self.playerMovement()
#         self.playerShoot()

#     def getxpos(self): # this function takes no parameters (not including self), and returns the players x-position
#         return self.rect.center[0]

#     def getypos(self): # this function takes no parameters (not including self), and returns the players y-position
#         return self.rect.center[1]

# plyr=Player(1,2,1,1,1,"C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/skeleton character frames.png") # object with placeholder arguments is created for testing purposes
# grpsngl=pygame.sprite.GroupSingle() #group is created to hold a single sprite. in this case, plyr so that it can be easily drawn
# grpsngl.add(plyr) # plyr object is added to the group


class Projectile(pygame.sprite.Sprite): # Projectile class, which is what the player will shoot

    def __init__(self,xpos,ypos, direct):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/BULLET.png").convert_alpha() # Image used
        self.rect = self.image.get_rect(center=(xpos,ypos)) # Projectile starting position

        self.direction = direct # What direction the projectile travels

    def moveProjectile(self,moverate): # Method that is used to move the projectile, depending on the self.direction attribute and by self.vel amount.

        if self.rect.x > 0 and self.rect.x < 1280 and self.rect.y > 0 and self.rect.y < 720: # This if statement will validate that the projectiles are on the screen. if not, they are deleted
            if self.direction == "up":
                self.rect.y-=moverate

            if self.direction == "down":
                self.rect.y+=moverate

            if self.direction == "left":
                self.rect.x -= moverate

            if self.direction == "right":
                self.rect.x += moverate

        else:
            pygame.sprite.Sprite.kill(self)
    def update(self,moverate):
        self.moveProjectile(moverate)

# projectilegroup = pygame.sprite.Group()



# while True: #Main game loop
#     screen.fill('black') #Background is given a colour, to draw over previous drawn player sprites
#     # listprojectiles = projectilegroup.sprites()
#     for event in pygame.event.get(): # iterates through what is returned from the pygame.event.get() function
        
#         if event.type==pygame.QUIT: # if the game is closed
#             pygame.quit()
#             sys.exit() # closes the game appropriately

#     for projectile in projectilegroup:
#         projectile.moveProjectile()
#     grpsngl.draw(screen) # plyr object is drawn on the screen
#     plyr.playerMovement() # plyr movement procedure is called, moving the player depending on the input
#     plyr.playerShoot()
#     projectilegroup.draw(screen)
#     pygame.display.update() # display is updated
#     clock.tick(60) # constant frames per second is set to 60
 