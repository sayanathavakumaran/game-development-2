import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("bday card")

img=pygame.image.load("14bday.jpg")
image = pygame.transform.scale(img, (WIDTH,HEIGHT))

while(True):
    font=pygame.font.SysFont("Brush Script",72)
    text=font.render("happy",True,(255,255,255))
    text2=font.render("birthday",True,(255,255,255))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text, (210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)

    image1=pygame.image.load("tealbg.jpg")
    font=pygame.font.SysFont("Ariel",80)
    text1=font.render("welcome home",True,(47,39,123))
    display_surface.fill((255,255,255))
    display_surface.blit(image1,(0,0))
    display_surface.blit(text1, (100,300))
    pygame.display.update()
    time.sleep(2)

    image2=pygame.image.load("xmas.jpg")
    image2=pygame.transform.scale(image2,(600,600))
    font=pygame.font.SysFont("Brush Script",85)
    text2=font.render("merry christmas",True,(255,255,255))
    display_surface.blit(image2,(0,0))
    display_surface.blit(text2, (85,200))
    pygame.display.update()
    time.sleep(2)