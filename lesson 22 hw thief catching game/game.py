import pygame
from pygame.locals import *
import time
import random

pygame.init()
screen = pygame.display.set_mode((800,800))
font1 = pygame.font.SysFont("Baskerville",35)
score = 0
text = font1.render("Score:  "+str(score),True,"black")

#class for police
class police(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("police.png")
        self.image=pygame.transform.scale(self.image,(50,55))
        self.rect=self.image.get_rect()

#class for thief
class thief(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("thief.png")
        self.image=pygame.transform.scale(self.image,(43,55))
        self.rect=self.image.get_rect()

#class for people
class people(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(30,55))
        self.rect=self.image.get_rect()

#list for recyclable items
list1 = ["boy.png","lady.png","oldman.png"]

#creating sprite groups
bad = pygame.sprite.Group()
good = pygame.sprite.Group()
all = pygame.sprite.Group()

#creating good people
for x in range(30):
    g_people = people(random.choice(list1))
    g_people.rect.x = random.randint(20,780)
    g_people.rect.y = random.randint(20,780)
    good.add(g_people)
    all.add(g_people)

#creating bad people
for x in range(20):
    b_people = thief()
    b_people.rect.x = random.randint(20,780)
    b_people.rect.y = random.randint(20,780)
    bad.add(b_people)
    all.add(b_people)

#object for police
police1 = police()
police1.rect.x = 20
police1.rect.y = 20
all.add(police1)

#background on screen
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,(800,800))

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        police1.rect.y -= 5
        if police1.rect.y <= 0:
            police1.rect.y = 0
    if keys[pygame.K_DOWN]:
        police1.rect.y += 5
        if police1.rect.y >= 730:
            police1.rect.y = 730
    if keys[pygame.K_RIGHT]:
        police1.rect.x += 5
        if police1.rect.x >= 735:
            police1.rect.x = 735
    if keys[pygame.K_LEFT]:
        police1.rect.x -= 5
        if police1.rect.x <= 0:
            police1.rect.x = 0
    police_good = pygame.sprite.spritecollide(police1,good,True)
    police_bad = pygame.sprite.spritecollide(police1,bad,True)
    for item in police_bad:
        score += 5
        text = font1.render("score: "+str(score),True,"black")
    for item in police_good:
        score -= 10
        text = font1.render("score: "+str(score),True,"black")

    screen.blit(bg,(0,0))
    screen.blit(text,(40,120))
    all.draw(screen)
    pygame.display.update()
pygame.quit()