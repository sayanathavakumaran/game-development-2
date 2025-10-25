import pygame
from pygame.locals import*

pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000,526))
bg = pygame.image.load("galaxy.jpg")
bg = pygame.transform.scale(bg,(1000,526))
left = pygame.image.load("left.png")
left = pygame.transform.scale(left,(70,39))
right = pygame.image.load("right.png")
right = pygame.transform.scale(right,(70,35))
#lbullet = pygame.image.load("leftbullet.png")
#lbullet = pygame.transform.scale(lbullet,(10,10))
#rbullet = pygame.image.load("rightbullet.png")
#rbullet = pygame.transform.scale(rbullet,(10,10))

#font
livefont = pygame.font.SysFont("Times New Roman",30)
overfont = pygame.font.SysFont("Times New Roman",50)

#gaming variables
fps = 60
velufo = 15
velbull = 20
border = pygame.Rect(495,0,10,800)
lhealth = 10
rhealth = 10
lbull = []
rbull = []

#class for ufo
class ufo(pygame.sprite.Sprite):
    def __init__(self,image,xpos,ypos):
        super().__init__()
        self.image=image
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
    #vertical movement
    def vert(self,sp):
        self.rect.move_ip(0,sp)
        if self.rect.top <=0 or self.rect.bottom >= 512:
                self.rect.move_ip(0,-sp)
    
    #horizontal movement
    def hori(self,sp,pl):
        if pl == 1: #left
            self.rect.move_ip(sp,0)
            if self.rect.left <=0 or self.rect.right >= border.left:
                self.rect.move_ip(-sp,0)   

        if pl == 2: #right
            self.rect.move_ip(sp,0)
            if self.rect.left <=border.right or self.rect.right >= 1000:
                self.rect.move_ip(-sp,0)

    
#creating object for the players
leftt = ufo(left,240,260)
rightt = ufo(right,740,260)

#creating sprite group
ufos = pygame.sprite.Group()
ufos.add(leftt)
ufos.add(rightt)

#function for window
def window():
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"black",border)
    #drawing health
    lhetext = livefont.render("health: "+str(lhealth),1,"white")
    rhetext = livefont.render("health: "+str(rhealth),1,"white")
    screen.blit(lhetext,(10,10))
    screen.blit(rhetext,(875,10))

#function for bullet
def bulldraw():
    for bullet in lbull:
        pygame.draw.rect(screen,"purple",bullet)
        bullet.x += velbull
    for bullet in rbull:
        pygame.draw.rect(screen,"white",bullet)
        bullet.x -= velbull

#handling the bullets
def handle():
    global lhealth,rhealth
    for bullet in lbull:
        if rightt.rect.colliderect(bullet):
            rhealth -= 1
            lbull.remove(bullet)
        elif bullet.x > 1000:
            lbull.remove(bullet)
    for bullet in rbull:
        if leftt.rect.colliderect(bullet):
            lhealth -= 1
            rbull.remove(bullet)
        elif bullet.x < 0:
            rbull.remove(bullet)
    for bullet1 in lbull:
        for bullet2 in rbull:
            if bullet1.colliderect(bullet2):
                lbull.remove(bullet1)
                rbull.remove(bullet2)

#function for winner
def winner(text):
    tdraw = overfont.render(text,1,"pink")
    screen.blit(tdraw,(265,100))
    pygame.display.update()
    pygame.time.delay(5000)
    

purplehit = pygame.USEREVENT+1
whitehit = pygame.USEREVENT+2

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_BACKSLASH:
                bullet = pygame.Rect(rightt.rect.x+10,rightt.rect.y+rightt.rect.height//2,20,10)
                rbull.append(bullet)
            if event.key == K_z:
                bullet = pygame.Rect(leftt.rect.x+35,leftt.rect.y+leftt.rect.height//2,20,10)
                lbull.append(bullet)
    #key pressed detection
    keyp = pygame.key.get_pressed()
    #left player movement
    if keyp[K_w]:
        leftt.vert(-5)
    if keyp[K_s]:
        leftt.vert(5)
    if keyp[K_a]:
        leftt.hori(-5,1)
    if keyp[K_d]:
        leftt.hori(5,1)
    #right player movement
    if keyp[K_UP]:
        rightt.vert(-5)
    if keyp[K_DOWN]:
        rightt.vert(5)
    if keyp[K_LEFT]:
        rightt.hori(-5,2)
    if keyp[K_RIGHT]:
        rightt.hori(5,2)
    window()
    ufos.draw(screen)
    bulldraw()
    handle()
    if rhealth == 0:
        text = "the left player has won !!"
        winner(text)
        run = False
    elif lhealth == 0:
        text = "the right player has won !!"
        winner(text)
        run = False
    pygame.display.update()
pygame.quit()
