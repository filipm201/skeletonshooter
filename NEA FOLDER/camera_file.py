import pygame, sys, player_class
from random import randint, choice
pygame.init() #pygame module is initialised
player_class.init()
clock = pygame.time.Clock() # clock variable can be used to easily measure time intervals
screenw=0
screenh=0
screen = pygame.display.set_mode((1920,1000))


class  Player(pygame.sprite.Sprite): # Player class is defined, and inherits from the pygame.sprite,Sprite class which comes from the pygame module
    def __init__(self, startingHealth, startingVelocityx, startingVelocityy, projectileSpeed,
startingFirerate, startingDamage, playerImage): # attributes of the player class are initialised in the constructor method
        super().__init__() #super method used to prevent any issues that may come from not using it
        self.image = pygame.image.load(playerImage) # self.image is a unique attribute and must be defined in a specific way, the pygame.sprite.Sprite is responsible for its unique behaviour
        self.rect = self.image.get_rect(center=(screenw,screenh)) # self.rect will be used to define and easily change the position of the player
        self.health = startingHealth
        self.velocityx = startingVelocityx
        self.velocityy = startingVelocityy
        self.reload = startingFirerate
        self.damage = startingDamage
        self.gunspeed = projectileSpeed
        self.playerDirection = pygame.math.Vector2() # creates a tuple (x, y) that can be used for directions

    def playerMovement(self): # A procedure responsible for the players movement, using the WASD keys
        tempkey = pygame.key.get_pressed()
        if tempkey[pygame.K_w]:
            self.playerDirection.y=-1
            self.rect.center+=self.playerDirection*self.velocityy # if w key is pressed, direction is defined as negative (due to how pygame coordinates work) and a value is added to the y coordinate of the players position
        elif tempkey[pygame.K_s]:
            self.playerDirection.y=1
            self.rect.center+=self.playerDirection*self.velocityy # opposite direction is chosen if s key is pressed, and added in same manner
        else:
            self.playerDirection.y=0 # direction is reset if there is no vertical movement key detected

        if tempkey[pygame.K_a]:
            self.playerDirection.x=-1
            self.rect.center+=self.playerDirection*self.velocityx # same process for a and d keys. d is positive direction, a is negative direction
        elif tempkey[pygame.K_d]:
            self.playerDirection.x=1
            self.rect.center+=self.playerDirection*self.velocityx
        else:
            self.playerDirection.x=0 # direction is reset if there is no horizontal movement key detected

plyr=Player(1,0.72,1.28,5,5,5,"C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/skeleton character frames.png") # object with placeholder arguments is created for testing purposes
grpsngl=pygame.sprite.GroupSingle() #group is created to hold a single sprite. in this case, plyr so that it can be easily drawn
grpsngl.add(plyr) # plyr object is added to the group

while True: #Main game loop
    screen.fill('black') #Background is given a colour, to draw over previous drawn player sprites
    for event in pygame.event.get(): # iterates through what is returned from the pygame.event.get() function
        if event.type==pygame.QUIT: # if the game is closed
            pygame.quit()
            sys.exit() # closes the game appropriately

    pygame.display.update() # display is updated
    clock.tick(60) # constant frames per second is set to 60
