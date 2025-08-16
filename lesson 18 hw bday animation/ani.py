import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("bday")

img1=pygame.image.load("red.jpg")
image1=pygame.transform.scale(img1, (WIDTH,HEIGHT))
img2=pygame.image.load("orange.jpg")
image2=pygame.transform.scale(img2, (WIDTH,HEIGHT))
img3=pygame.image.load("yellow.jpg")
image3=pygame.transform.scale(img3, (WIDTH,HEIGHT))
img4=pygame.image.load("green.jpg")
image4=pygame.transform.scale(img4, (WIDTH,HEIGHT))
img5=pygame.image.load("teal.jpg")
image5=pygame.transform.scale(img5, (WIDTH,HEIGHT))
img6=pygame.image.load("blue.webp")
image6=pygame.transform.scale(img6, (WIDTH,HEIGHT))
img7=pygame.image.load("navy.jpg")
image7=pygame.transform.scale(img7, (WIDTH,HEIGHT))
img8=pygame.image.load("purple.jpg")
image8=pygame.transform.scale(img8, (WIDTH,HEIGHT))
img9=pygame.image.load("lilac.jpg")
image9=pygame.transform.scale(img9, (WIDTH,HEIGHT))
img10=pygame.image.load("lipink.webp")
image10=pygame.transform.scale(img10, (WIDTH,HEIGHT))
img11=pygame.image.load("pink.webp")
image11=pygame.transform.scale(img11, (WIDTH,HEIGHT))
img12=pygame.image.load("coral.jpg")
image12=pygame.transform.scale(img12, (WIDTH,HEIGHT))
img13=pygame.image.load("gold.jpg")
image13=pygame.transform.scale(img13, (WIDTH,HEIGHT))

while(True):
    font=pygame.font.SysFont("Brush Script",72)
    text1 = font.render("h",True,(255,255,255))
    display_surface.blit(image1,(0,0))
    display_surface.blit(text1,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text2 = font.render("ha",True,(255,255,255))
    display_surface.blit(image2,(0,0))
    display_surface.blit(text2,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text3 = font.render("hap",True,(255,255,255))
    display_surface.blit(image3,(0,0))
    display_surface.blit(text3,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text4 = font.render("happ",True,(255,255,255))
    display_surface.blit(image4,(0,0))
    display_surface.blit(text4,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text5 = font.render("happy",True,(255,255,255))
    display_surface.blit(image5,(0,0))
    display_surface.blit(text5,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text6 = font.render("happy b",True,(255,255,255))
    display_surface.blit(image6,(0,0))
    display_surface.blit(text6,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text7 = font.render("happy bi",True,(255,255,255))
    display_surface.blit(image7,(0,0))
    display_surface.blit(text7,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text8 = font.render("happy bir",True,(255,255,255))
    display_surface.blit(image8,(0,0))
    display_surface.blit(text8,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text9 = font.render("happy birt",True,(255,255,255))
    display_surface.blit(image9,(0,0))
    display_surface.blit(text9,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text10 = font.render("happy birth",True,(255,255,255))
    display_surface.blit(image10,(0,0))
    display_surface.blit(text10,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text11 = font.render("happy birthd",True,(255,255,255))
    display_surface.blit(image11,(0,0))
    display_surface.blit(text11,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text12 = font.render("happy birthda",True,(255,255,255))
    display_surface.blit(image12,(0,0))
    display_surface.blit(text12,(150,250))
    pygame.display.update()
    time.sleep(0.5)

    font=pygame.font.SysFont("Brush Script",72)
    text13 = font.render("happy birthday",True,(255,255,255))
    display_surface.blit(image13,(0,0))
    display_surface.blit(text13,(150,250))
    pygame.display.update()
    time.sleep(2)





