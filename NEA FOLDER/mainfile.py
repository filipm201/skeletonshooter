# file path for images is: C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA
import pygame, sys
from random import randint, choice
pygame.init()
from projectile_class import Projectile
from obstacle_class import Obstacle
from enemy_class import Enemy
from player_class import Player
#variables
clock = pygame.time.Clock()

gameState = "menu"

#screen management

screen = pygame.display.set_mode((1280,720)) # variable screen is assigned as the surface on which everything will be. 
mainmenuscreen = pygame.image.load("C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/mainmenu.jpg") #images are loaded through pygames and assigned to pygame variables.
#This is so that they do not have to be loaded multiple times which would waste resources.
gameoverscreen = pygame.image.load("C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/gameover.jpg")
bgimage=pygame.image.load("C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/background.jpg")
pausescreen=pygame.image.load("C:/Users/Filip201/OneDrive/Documents/Desktop/NEA FOLDER/Images NEA/background.jpg")
ENEMYSPWN = pygame.USEREVENT + 1 # New userevent is created
pygame.time.set_timer(ENEMYSPWN,1000) # every 1000 milliseconds, the event happens. This will be caught in for loops as seen later
plyr=Player(50,5,5,5,5) # object with placeholder arguments is created for testing purposes
grpsngl=pygame.sprite.GroupSingle() #group is created to hold a single sprite. in this case, plyr so that it can be easily drawn and treated as a pygame sprite
grpsngl.add(plyr) # plyr object is added to the group
obstGroup = pygame.sprite.Group() # Group is created for each respective class
projectilegroup = pygame.sprite.Group()
enemygroup = pygame.sprite.Group()
pickupgroup = pygame.sprite.Group()
obstGroup.add(Obstacle(randint(0,1280), randint(0,720)) for x in range(0,20)) # A comprehension to create and randomly place 40 obstacles.
score=0 # score variable which will be the players score system is set to 0 as starting value
font=pygame.font.Font(None,40) # font that will be used is set


with open("leaderboard.txt","r+") as fwrite:
    if not fwrite.readline().strip():
        fwrite.write(f'0')
highscore = int(open("leaderboard.txt","r").readline().strip()) #The highscore is the first line of the file, and set as an integer so that it can be compared to the score after the game

# has ended
print(highscore)



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

            if event.type == pygame.KEYDOWN and keydetection[pygame.K_p]:
                pause=True
                while pause:
                    screen.blit(pausescreen,(0,0))
                    keydetection=pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and keydetection[pygame.K_p]:
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
            pygame.sprite.Sprite.kill(plyr)
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
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        keydetection = pygame.key.get_pressed()
        if keydetection[pygame.K_r]:
            gameState="activeGame"

        if keydetection[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    
        screen.blit(gameoverscreen,(0,0))
        pygame.display.flip() 

    # if gameState == "tutorial": # tutorial state of the game
    #     for event in pygame.event.get():
    #         if event.type==pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == pygame.K_t:
    #             gameState = "activeGame" # changes gamestate when the T key is pressed back to the active game

        pygame.display.flip() 