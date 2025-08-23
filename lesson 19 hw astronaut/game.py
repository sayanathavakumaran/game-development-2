import pygame
from pygame.locals import*
from time import*

pygame.init()
screen = pygame.display.set_mode((900,550))

space = pygame.image.load("space.jpg")
space = pygame.transform.scale(space,(900,550))
astro = pygame.image.load("astro.webp")
astro = pygame.transform.scale(astro,(100,100))
x = 420
y = 225
run = True
up = False
down = False
right = False
left = False
while y<550:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
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
    if up and y > 0:
        y -= 18
    if down and y < 550:
        y += 10
    if right and x > 0:
        x += 10
    if left and x < 550:
        x -= 10
    screen.blit(space,(0,0))
    screen.blit(astro,(x,y))
    pygame.display.update()
    y += 8
    sleep(0.07)

print("game over !!")