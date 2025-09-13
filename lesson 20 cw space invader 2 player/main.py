import pygame
from pygame.locals import*

pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000,526))
bg = pygame.image.load("galaxy.jpg")
bg = pygame.transform.scale(bg,(1000,526))
left = pygame.image.load("left.png")
left = pygame.transform.scale(left,(50,50))
right = pygame.image.load("right.png")
right = pygame.transform.scale(right,(50,50))
lbullet = pygame.image.load("leftbullet.png")
lbullet = pygame.transform.scale(lbullet,(10,10))
rbullet = pygame.image.load("rightbullet.png")
rbullet = pygame.transform.scale(rbullet,(10,10))

#font
livefont = pygame.font.SysFont("Pixelify Sans",30)
overfont = pygame.font.SysFont("Pixelify Sans",50)

#gaming variables
fps = 60
velufo = 15
velbull = 20
border = pygame.Rect(495,0,10,800)
lhealth = 10
rhealth = 10

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        screen.blit(bg,(0,0))
        pygame.draw.rect(screen,"white",border)
    pygame.display.update()
pygame.quit()