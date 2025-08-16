import pygame
from pygame.locals import*
from time import*

pygame.init()
screen = pygame.display.set_mode((900,550))

sky = pygame.image.load("sky.jpg")
sky = pygame.transform.scale(sky,(900,550))
balloon = pygame.image.load("balloon.png")
balloon = pygame.transform.scale(balloon,(100,100))
x = 420
y = 225
run = True
up = False
left = False
right = False
down = False
while y<550:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #run = False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                up = True
            if event.key==K_DOWN:
                down = True
            if event.key==K_RIGHT:
                right = True
            if event.key==K_LEFT:
                left = True
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                up = False
            if event.key==K_DOWN:
                down = False
            if event.key==K_RIGHT:
                right = False
            if event.key==K_LEFT:
                left = False
    #movement logic
    if up and y > 0:
        y -= 12
    if down and y < 550:
        y += 12
    if left and x > 0:
        x -= 12
    if right and x < 810:
        x += 12    
    screen.blit(sky,(0,0))
    screen.blit(balloon,(x,y))
    pygame.display.update()
    y += 8
    sleep(0.08)

print("game over !!")
   


