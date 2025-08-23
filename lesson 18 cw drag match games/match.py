import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill("black")
pygame.display.update()
#load images
fplay = pygame.image.load("4 player.webp")
fplay = pygame.transform.scale(fplay,(90,90))
screen.blit(fplay,(70,35))
bblast = pygame.image.load("block blast.jpg")
bblast = pygame.transform.scale(bblast,(90,90))
screen.blit(bblast,(70,155))
mine = pygame.image.load("minecraft.png")
mine = pygame.transform.scale(mine,(90,90))
screen.blit(mine,(70,265))
rob = pygame.image.load("roblox.png")
rob = pygame.transform.scale(rob,(90,90))
screen.blit(rob,(70,385))
pygame.display.update()

#creating text
font1 = pygame.font.SysFont("Times New Roman",30)
text1 = font1.render("minecraft",1,(255,255,255))
screen.blit(text1,(340,55))
text2 = font1.render("4 player",1,(255,255,255))
screen.blit(text2,(340,180))
text3 = font1.render("roblox",1,(255,255,255))
screen.blit(text3,(340,290))
text4 = font1.render("block blast",1,(255,255,255))
screen.blit(text4,(340,410))
pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        #dragging to match
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,"red",(mousepos),10,0)
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            mousepos1 = pygame.mouse.get_pos()
            pygame.draw.line(screen,"red",(mousepos),(mousepos1),5)
            pygame.draw.circle(screen,("red"),(mousepos1),10,0)
            pygame.display.update()
pygame.quit()

