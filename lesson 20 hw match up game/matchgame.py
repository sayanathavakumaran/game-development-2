import pygame

pygame.init()
screen = pygame.display.set_mode((500,650))
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
matiles = pygame.image.load("magic tiles.jpg")
matiles = pygame.transform.scale(matiles,(90,90))
screen.blit(matiles,(70,520))
pygame.display.update()

#creating text
font1 = pygame.font.SysFont("Impact",37)
font2 = pygame.font.SysFont("Bodoni",28)
font3 = pygame.font.SysFont("Copperplate Gothic",30,bold=True)
font4 = pygame.font.SysFont("Rockwell",28)
font5 = pygame.font.SysFont("Comic Sans",32,bold=True)
text1 = font1.render("MINECRAFT",0,(121,71,28))
screen.blit(text1,(300,55))
text2 = font2.render("magic tiles 3",1,(255,0,255))
screen.blit(text2,(300,180))
text3 = font3.render("ROBLOX",1,(0,0,255))
screen.blit(text3,(300,300))
text4 = font4.render("BLOCK BLAST",1,(255,35,150))
screen.blit(text4,(300,420))
text5 = font5.render("4 player",1,(0,255,100))
screen.blit(text5,(300,540))
pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        #dragging to match
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            pygame.draw.rect(screen,"blue",(*mousepos,20,20))
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            mousepos1 = pygame.mouse.get_pos()
            pygame.draw.line(screen,"blue",(mousepos),(mousepos1),5)
            pygame.draw.rect(screen,"blue",(*mousepos1,20,20))
            pygame.display.update()
pygame.quit()

