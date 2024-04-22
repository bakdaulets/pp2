#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
cnt = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):

        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

class Coins(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f'coin.png') 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(10, 390), 25) 
    
    def move(self):
        self.rect.move_ip(0, 5) 
        if self.rect.bottom > 600:
            self.rect.top = 0 
            self.rect.center = (random.randint(20, 360), 10)
            self.image = pygame.image.load(f'coin.png')

class BonusCoins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f'bcoin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, 390), 10)
        self.c = 0
            
    def move(self):
        self.rect.move_ip(0,2)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(20, 360), 10)
            self.image = pygame.image.load(f'bcoin.png')
            self.c = 0 


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coins()
B1 = BonusCoins()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
bonus =  pygame.sprite.Group()
bonus.add(B1)
all_sprites = pygame.sprite.Group()
new_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
new_sprites.add(B1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    score = font_small.render(str(cnt), True, RED )
    DISPLAYSURF.blit(score, (370,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

        #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(1)
                   
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,60))
            print(f"tour score is: {cnt}")
            
            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()
        #Generate bonus coin
        if B1.c  ==  3:
            for things in new_sprites:
                DISPLAYSURF.blit(things.image, things.rect)
                things.move()        
        
        if pygame.sprite.spritecollideany(P1, coins):
            cnt += 1
            C1.rect.top = 600
            B1.c +=1
            #Increasing the speed every 3 coins
            if cnt % 3 == 0:
                SPEED += 1.2
        if pygame.sprite.spritecollideany(P1, bonus):
            cnt += 2
            B1.rect.top = 600
            B1.c = 0 

    pygame.display.update()
    pygame.display.flip()
    FramePerSec.tick(FPS)
