#Import the basic libraries
import os
import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()
FPS = 60

pygame.init()
pygame.font.init()

#Game Music

pygame.mixer.init()
pygame.mixer.music.load("Gaming music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

#Colors

BLACK = (0,0,0)
PURPLE = (200,0,255)
COLOR = (0,155,200)
COLORB=(240,20,100)

#Setting the window faetures and the backround

win_width=700
win_height=500

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pong")
background = pygame.transform.scale(pygame.image.load("Court2.png"),(win_width,win_height))
window.blit(background,(0, 0))
 
#Class for the paddles
class Paddle(pygame.sprite.Sprite):
    def __init__(self,color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()

        #The moving functions
    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

paddleA = Paddle(PURPLE, 10, 100)
paddleA.rect.x = 0
paddleA.rect.y = 200

paddleB = Paddle(COLORB, 10, 100)
paddleB.rect.x = 690
paddleB.rect.y = 200
 
#The group list of sprites
all_sprites_list = pygame.sprite.Group()

#The Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self,ball_image,ball_x,ball_y,ball_speed,speed_x,speed_y):
        super().__init__()
        self.image = ball_image
        self.speed=ball_speed
        self.rect=self.image.get_rect()
        self.rect.y=ball_y
        self.rect.x=ball_x
        self.speedx=speed_x
        self.speedy=speed_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Class for the moovement of the ball
class BallMove(Ball):
    def update(self):
        self.rect.y += self.speedy
        self.rect.x -= self.speedx
        if self.rect.y >= 460:
            self.speedy *= -1
        if self.rect.y == -20:
            self.speedy *= -1

ball_image=pygame.transform.scale(pygame.image.load('PongBall2.png'), (60, 50))
ball_x = 320
ball_y = 200
ball_speed=speed_x=speed_y=5
ball = BallMove(ball_image,ball_x,ball_y,ball_speed,speed_y,speed_x)

#Adding the paddles and the ball in the sprite list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#Setting score values
scoreA=0
scoreB=0

#Winning images for every player
play1_win=pygame.transform.scale(pygame.image.load('pl1.png'), (300, 200))
play2_win=pygame.transform.scale(pygame.image.load('Win22.png'), (500, 200))

#The game loop
game =True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.blit(background,(0, 0))

    #Keys for mooving paddles upsdie down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    #Scoring System
    if ball.rect.x >= 660:
        scoreA += 1
        ball.speedx *= -1
        score_snd=pygame.mixer.Sound("ScoreSound.mp3")
        inicial_som = pygame.mixer.Sound((os.path.join('ScoreSound.mp3')))
        score_snd.play()
    if ball.rect.x == -20:
        scoreB += 1
        ball.speedx *= -1
        score_snd=pygame.mixer.Sound("ScoreSound.mp3")
        inicial_som = pygame.mixer.Sound((os.path.join('ScoreSound.mp3')))
        score_snd.play()

    #Fonts for score

    font1 = pygame.font.Font(None, 60)
    score = font1.render(str(scoreA) , 1, (0, 50, 255))
    window.blit(score,(130,30))
    
    font2 = pygame.font.Font(None, 60)
    score = font2.render(str(scoreB) , 1, (100, 255, 255))
    window.blit(score,(540,30))

    #Winning sprites for player 1 and player 2

    if scoreA==10:
        window.blit(play1_win,(50,100))
        ball.rect.x=325
        ball.rect.y=200
        paddleA.rect.y=200
        paddleB.rect.y=200
    if scoreB==10:
        window.blit(play2_win,(250,80))
        ball.rect.x=315
        ball.rect.y=200
        paddleB.rect.y=200
        paddleA.rect.y=200

    #Collide conditions with baddle and ball

    if pygame.sprite.collide_mask(ball, paddleA):
        ball.speedx=ball.speedx * -1
        paddle_snd=pygame.mixer.Sound("PaddleSound.mp3")
        inicial_som = pygame.mixer.Sound((os.path.join('PaddleSound.mp3')))
        paddle_snd.play()
    if pygame.sprite.collide_mask(ball, paddleB):
        ball.speedx=ball.speedx * -1
        paddle_snd=pygame.mixer.Sound("PaddleSound.mp3")
        inicial_som = pygame.mixer.Sound((os.path.join('PaddleSound.mp3')))
        paddle_snd.play()

    #Update the sprite list
    all_sprites_list.update()

    ball.reset()

    #Draw the net
    pygame.draw.line(window, COLOR, (349, 0), (349, 500), 5)
    
    #Display the Sprites on screen
    all_sprites_list.draw(window) 

    clock.tick(FPS)
    pygame.display.update()