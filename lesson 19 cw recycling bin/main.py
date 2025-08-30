import pygame
from pygame.locals import *
import time
import random

pygame.init()
screen = pygame.display.set_mode((800,800))

#class for bin
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()

#class for plastic bag
class plastic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plastic.webp")
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

#class for foods
class foods(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()


#list for recyclable items
list1 = ["apple.png","banana.webp","blueberry.png","pepper.png"]

#creating sprite groups
non_recy = pygame.sprite.Group()
recy = pygame.sprite.Group()
items = pygame.sprite.Group()

#creating recyclable items
for x in range(35):
    r_item = foods(random.choice(list1))
    r_item.x = random.randint(20,780)
    r_item.y = random.randint(20,780)
    recy.add(r_item)
    items.add(r_item)

run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        items.draw(screen)
    pygame.display.update()
pygame.quit()
