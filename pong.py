import pygame
import time
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((1280,720))
done = False
#set initial variables
p1_x,p1_y=30,30
p2_x,p2_y=(screen.get_width()-60),30
ball_x,ball_y=((screen.get_width())/2),((screen.get_height())/2)
slope_x,slope_y=2,2
paddle_score=0
#set constants
paddle_width = screen.get_width()/64
paddle_height = screen.get_height()/3.6
#define Paddle class
class Paddle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.player=pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,paddle_width,paddle_height))
        self.rect=pygame.Rect(self.x,self.y,paddle_width,paddle_height)

        #macros
        self.paddle_speed=3

    def draw(self):
        self.player=pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,paddle_width,paddle_height))
        self.rect=pygame.Rect(self.x,self.y,paddle_width,paddle_height)
    def up(self):
        if self.y>0:
            self.y-=self.paddle_speed
    def down(self):
        if self.y<screen.get_height()-paddle_height: 
            self.y+=self.paddle_speed
#define ball class
class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.slope_x=slope_x
        self.slope_y=slope_y
        self.ball=pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,paddle_width,paddle_width))
        self.rect = pygame.Rect(self.x,self.y,paddle_width,paddle_width)
        self.ball_score=0
        self.paddle_score=0
        #macros
        self.ball_speed=1.2

    def draw(self):
        #make ball movement
        self.x+=self.slope_x
        if self.y <= 0 or self.y >= (screen.get_height()):
            self.slope_y*=-1
        if self.x <= 0:
            self.slope_x*=-1
            self.ball_score+=1
            self.x,self.y=((screen.get_width())/2),((screen.get_height())/2)
            time.sleep(1)
        if self.x >= (screen.get_width()):
            self.slope_x*=-1
            self.ball_score+=1
            self.x,self.y=((screen.get_width())/2),((screen.get_height())/2)
            time.sleep(1)
        #collision
        self.rect = pygame.Rect(self.x,self.y,paddle_width,paddle_width)
        if self.rect.colliderect(p1.rect): self.col(p1) 
        if self.rect.colliderect(p2.rect): self.col(p2)
        self.player=pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x,self.y,paddle_width,paddle_width))
        self.rect = pygame.Rect(self.x,self.y,paddle_width,paddle_width)

    def col(self,obj):

        if self.slope_x > 0: # Moving right; Hit the left side of the paddle
            self.rect.right = obj.rect.left
        if self.slope_x < 0: # Moving left; Hit the right side of the paddle
            self.rect.left = obj.rect.right
        self.paddle_score+=1
        self.slope_x*=-1
        if self.slope_y>0:
            self.slope_y=random.randint(1,3) * -1
        else:
            self.slope_y=random.randint(1,3)
        self.x+=(self.slope_x*2)
        self.y+=self.slope_y
    def up(self):
        if self.y>0:
            self.y-=self.ball_speed
    def down(self):
        if self.y<screen.get_height()-paddle_width: 
            self.y+=self.ball_speed


#set initial conditions
p1_score,p2_score=0,0
p1=Paddle(p1_x,p1_y)
p2=Paddle(p2_x,p2_y)
ball=Ball(ball_x,ball_y)

#main loop

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    
    #controls
    #paddles
    if pressed[pygame.K_w]:
        p1.up()
        p2.up()
    if pressed[pygame.K_s]:
        p1.down()
        p2.down()
    #ball
    if pressed[pygame.K_UP]:
        ball.up()
    if pressed[pygame.K_DOWN]:
        ball.down()

    #make players and ball
    screen.fill((0,0,0))
    score = myfont.render(str(p1_score)+" "+str(p2_score), True, (255,255,255))
    screen.blit(score, ((screen.get_width()/2)-20,0))
    p1.draw()
    p2.draw()
    ball.draw()

    pygame.display.flip()
