# file path for images is: C:/Users/Filip201/myrepos/skeleton shooter/NEA FOLDER
import pygame, sys
from random import randint
pygame.init()

#variables
clock = pygame.time.Clock()

gameState = "menu"

class button(pygame.sprite.Sprite):
    def __init__(self,givenxpos,givenypos,widthheight,colour,textonbutton):
        super().__init__()
        #whatever text will be in it, what colour and then combined into one.
        fontused=pygame.font.SysFont('Calibri',10,False,False)

        self.image = fontused.render(str(textonbutton),True,'Black',widthheight)
        self.rect = pygame.image.get_rect(center=(givenxpos,givenypos))
        self.image.fill(colour)
        
class Pickup(pygame.sprite.Sprite):

    def __init__(self,givenpos):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill((randint(0,100),randint(0,100),randint(0,100)))
        self.rect = self.image.get_rect(center=(givenpos))


clock = pygame.time.Clock()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, randPosx, randPosy): # when an obstacle object is created, it will take 2 parameters for where its position will be. This is the only thing that will differ-
        #- between obstacle objects, everything else will be standardised.
        super().__init__()
        self.image=pygame.image.load('C:/Users/Filip201/myrepos/skeletonshooter/NEA FOLDER/Images NEA/basic environment obstacles.png')
        self.rect=self.image.get_rect(center=(randPosx,randPosy)) # It will be placed in the parameters given

class  Player(pygame.sprite.Sprite): # Player class is defined, and inherits from the pygame.sprite,Sprite class which comes from the pygame module
    def __init__(self, startingHealth, startingVelocity, projectileSpeed, startingFirerate, startingDamage): # attributes of the player class are initialised in the constructor method
        super().__init__() #super method used to prevent any issues that may come from not using it
        self.image = pygame.image.load("C:/Users/Filip201/myrepos/skeletonshooter/NEA FOLDER/Images NEA/character.png") 
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
            self.playerDirection.y=-1 # if w key is pressed, direction is defined as negative (due to how pygame coordinates work) and a value is added to the y coordinate of the players position

        elif tempkey[pygame.K_s]:
                self.playerDirection.y=1 # opposite direction is chosen if s key is pressed, and added in same manner
        else:
            self.playerDirection.y=0 # direction is reset if there is no vertical movement key detected

        self.rect.centery+=self.playerDirection[1]*self.velocity

        if pygame.sprite.spritecollide(self,obstgroup,False,collided=None):
            self.rect.centery = holdvaluey
        if tempkey[pygame.K_a]:
            self.playerDirection.x=-1 # same process for a and d keys. d is positive direction, a is negative direction

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
            if key[pygame.K_UP]: # Projectile is created, with a different direction depending on what key is pressed.
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
                self.health+=5
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

class Projectile(pygame.sprite.Sprite): # Projectile class, which is what the player will shoot

    def __init__(self,xpos,ypos, direct):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Filip201/myrepos/skeletonshooter/NEA FOLDER/Images NEA/BULLET.png").convert_alpha() # Image used
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self,givenVelocityx,givenVelocityy):
        super().__init__()

        self.velocityx=givenVelocityx
        self.velocityy=givenVelocityy
        self.image=pygame.image.load("C:/Users/Filip201/myrepos/skeletonshooter/NEA FOLDER/Images NEA/skeleton front view.png")
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

#screen management

screen = pygame.display.set_mode((1280,720)) # variable screen is assigned as the surface on which everything will be. 
mainmenuscreen = pygame.image.load("C:/Users/Filip201/myrepos/skeletonshooter/NEA FOLDER/Images NEA/mainmenu.jpg") #images are loaded through pygame and assigned to variables to save resources

score = 0 # score variable which will be the players score system is set to 0 as starting value
font = pygame.font.Font(None,40) # font that will be used is set


gameoverscreen = pygame.image.load("C:/Users/Filip201/myrepos/skeletonshooter/NEA FOLDER/Images NEA/gameover.jpg")
bgimage=pygame.image.load("C:/Users/Filip201/myrepos/skeletonshooter/NEA FOLDER/Images NEA/background.jpg")
pausescreen=pygame.image.load("C:/Users/Filip201/myrepos/skeletonshooter/NEA FOLDER/Images NEA/pause screen.jpg")

ENEMYSPWN = pygame.USEREVENT + 1 # New userevent is created
pygame.time.set_timer(ENEMYSPWN,1000) # every 1000 milliseconds, the event happens. This will be caught in for loops as seen later

plyr = Player(50,5,5,5,5) # object with placeholder arguments is created for testing purposes
grpsngl=pygame.sprite.GroupSingle() #group is created to hold a single sprite. in this case, plyr so that it can be easily drawn and treated as a pygame sprite
grpsngl.add(plyr) # plyr object is added to the group
obstGroup = pygame.sprite.Group() # Group is created for each respective class
projectilegroup = pygame.sprite.Group()
enemygroup = pygame.sprite.Group()
pickupgroup = pygame.sprite.Group()
obstGroup.add(Obstacle(randint(0,1280), randint(0,720)) for x in range(0,20)) # A comprehension to create and randomly place 40 obstacles.




with open("leaderboard.txt","r+") as fwrite:
    if not fwrite.readline().strip():
        fwrite.write(f'0')
highscore = int(open("leaderboard.txt","r").readline().strip()) #The highscore is the first line of the file, and set as an integer so that it can be compared to the score after the game

while True: # main game loop

    while gameState == "menu": # Following code will execute when on the menuscreen
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(mainmenuscreen,(0,0)) # draws main menu graphic
        
        keydetection=pygame.key.get_pressed() #variable that is the key pressed by the user

        if keydetection[pygame.K_SPACE]:
            gameState = "activeGame" # will start the game
        if keydetection[pygame.K_ESCAPE]:
            pygame.quit() # will close the game
            sys.exit()

        pygame.display.flip() # updates the game of the screen

    while gameState == "activeGame":

        screen.blit(bgimage,(0,0)) # displays the background image
        keydetection=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ENEMYSPWN: # every 1000 milliseconds, this event is caught and another enemy object is added to enemygroup
                enemygroup.add(Enemy(1,1))

            if keydetection[pygame.K_p]:
                pause=True
                while pause:
                    screen.blit(pausescreen,(0,0))
                    keydetection=pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if keydetection[pygame.K_p]:
                            pause = False
                    if keydetection[pygame.K_ESCAPE]:
                        pygame.quit()
                        sys.exit()
                    print(gameState)

                    #image that says press p to unpause

                    clock.tick(60)
                    pygame.display.flip()
        
        print(clock.get_fps())
        
        grpsngl.update(obstGroup,projectilegroup,pickupgroup,screen)
        plyr.takeDmg(enemygroup)
        enemygroup.update(plyr)
        
        for enemy in enemygroup:
            score+=enemy.takeDamage(projectilegroup,pickupgroup,plyr.damage)

        if plyr.health <=0:
            grpsngl.empty()
            gameState = "gameOver"
            with open("leaderboard.txt","w") as file:
                if score > int(highscore):
                    file.write(f'{score}')

        obstGroup.draw(screen) # groups are drawn on screen
        grpsngl.draw(screen)
        pickupgroup.draw(screen)
        projectilegroup.draw(screen)
        enemygroup.draw(screen)

        rendfont=font.render(f'Current score: {score}',True,(3,30,30))
        highscoreoutput=font.render(f'Highscore: {highscore}',True,(3,30,30))

        screen.blit(rendfont,(100,100))
        screen.blit(highscoreoutput,(100,200))

        clock.tick(60)
        pygame.display.flip() 
    obstGroup.empty()
    
    enemygroup.empty()
        

    while gameState=="gameOver": # game over screen state of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keydetection = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN and keydetection[pygame.K_r]:
                gameState="activeGame"
                plyr = Player(50,5,5,5,5) # object with placeholder arguments is created for testing purposes
                grpsngl.add(plyr)

            if  event.type == pygame.KEYDOWN and keydetection[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
    
        screen.blit(gameoverscreen,(0,0))
        pygame.display.flip() 
