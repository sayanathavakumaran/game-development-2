import pygame
import random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
fps = 60
sw = 864
sh = 700
screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("FLAPPY BIRD")
font1 = pygame.font.SysFont("Bauhaus 93",80)

#gaming variables

groscroll = 0
scrospeed = 4
flying = False
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
    def update(self):
        global flying, gameover
        if flying:
            self.velocity += 0.2
            if self.velocity > 4:
                self.velocity = 4
            if self.rect.bottom < 600:
                self.rect.y += int(self.velocity)
        #if game is not over
        if not gameover:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.velocity = -7
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            #animating the bird
            flap = 40
            self.counter += 1
            if self.counter > flap:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
            #rotating bird according to movement
            self.image = pygame.transform.rotate(self.images[self.index],self.velocity*-2)
        else:
            if self.rect.bottom > 600:
                self.image = pygame.transform.rotate(self.images[self.index],0)
            else:
                self.image = pygame.transform.rotate(self.images[self.index],-90)
class pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,updown):
        super().__init__()
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()
        #position 1 = top, position -1 = bottom
        if updown == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-int(pipegap/2)]
        elif updown == -1:
            self.rect.topleft = [x,y+int(pipegap/2)]
    def update(self):
        self.rect.x -= scrospeed
        if self.rect.right < 0:
            self.kill()

pipegroup = pygame.sprite.Group()

#reset function

def reset():
    pipegroup.empty()
    birdd.rect.x = 100
    birdd.rect.y = 432
    score = 0
    return score

class resetbutton():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def draw(self):
        resetclicked = False
        mousepos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousepos):
            if pygame.mouse.get_pressed()[0] == 1:
                resetclicked = True
        screen.blit(self.image,(self.rect.x-10,self.rect.y))
        return resetclicked
    
resetbuttonn = resetbutton(432,350,restart)

#bird object

birdd = bird(100,432)
birdgroup = pygame.sprite.Group()
birdgroup.add(birdd)

run = True
while run:
    clock.tick(fps)
    #collision detection
    if pygame.sprite.groupcollide(birdgroup,pipegroup,False,False) or birdd.rect.top<0 or birdd.rect.bottom>700:
        gameover = True

    #pipe generation and scrolling
    if flying and not gameover:
        currenttime = pygame.time.get_ticks()
        if currenttime - lastpipetime > pipefreq:
            pipeheight = random.randint(-100,100)
            bottompipe = pipes(sw,int(sh//2)+pipeheight,-1)
            toppipe = pipes(sw,int(sh//2)+pipeheight,1)
            pipegroup.add(bottompipe)
            pipegroup.add(toppipe)
            lastpipetime = currenttime
        pipegroup.update()
        groscroll -= scrospeed
        if abs(groscroll) > 30:
            groscroll = 0 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not gameover:
            flying = True
    screen.blit(bg,(0,0))
    pipegroup.draw(screen)
    screen.blit(ground,(groscroll,600))
    birdgroup.draw(screen)
    birdgroup.update()
    if gameover == True:
        if resetbuttonn.draw():
            gameover = False
            score = reset()
    if len(pipegroup) > 0:
        birddd = birdgroup.sprites()[0]
        pipess = pipegroup.sprites()[0]
        if birddd.rect.left > pipess.rect.left and birddd.rect.right < pipess.rect.right and not birdpasspipe:
            birdpasspipe = True
        if birdpasspipe and birddd.rect.left > pipess.rect.right:
            score += 1
            birdpasspipe = False
        text = font1.render(str(score),True,"white")
        screen.blit(text,(407,20))
    pygame.display.update()
pygame.quit()
