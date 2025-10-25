import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((864,700))
pygame.display.set_caption("FLAPPY BIRD")
font1 = pygame.font.SysFont("Bauhaus 93",45)

#gaming variables

groscroll = 0
scrospeed = 6
starttrack = False
gameover = False
pipegap = 150
pipefreq = 2000
lastpipetime = pygame.time.get_ticks() - pipefreq
score = 0
birdpasspipe = False

#loading images

ground = pygame.image.load("ground.png")
bg = pygame.image.load("bg.png")
restart = pygame.image.load("restart.png")

#bird class
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0
        #loading bird images
        for i in range(1,4):
            birds = pygame.image.load(f"bird{i}.png")
            self.images.append(birds)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0
        self.clicked = False

#bird object

birdd = bird(160,400)
birdgroup = pygame.sprite.Group()
birdgroup.add(birdd)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    #pygame.display.update()
pygame.quit()
