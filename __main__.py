import pygame
import time
import random
from pong import *

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
#set constants
paddle_width = screen.get_width()/64
paddle_height = screen.get_height()/3.6

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