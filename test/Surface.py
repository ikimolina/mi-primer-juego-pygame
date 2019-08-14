import sys
import pygame


pygame.init()


width = 400
height = 500


surface = pygame.display.set_mode ( (width,height) )
pygame.display.set_caption("Hola Mundo")


red =  pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(80,0,255)
violet = pygame.Color(169,18,164)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

pygame.mixer.music.load("Mp3/SHOVEL.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1,0.0)
font = pygame.font.Font("freesansbold.ttf",48)

rect1  = pygame.Rect(0,0,100,80)
rect1.center = (width//2,height//2)

rect2 = pygame.Rect(0,0,100,80)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    surface.fill(black)
    
    rect2.center = pygame.mouse.get_pos()
    
    pygame.draw.rect(surface,green,rect1)
    pygame.draw.rect(surface,red,rect2)
    
    message = ""
    
    
    if rect1.colliderect(rect2):
        message = "Colisión"
    
    text = font.render(message,True,blue)
    rect3 = text.get_rect()
    rect3.midtop = (width//2,50)
    
    surface.blit(text,rect3)
    
    seconds = pygame.time.get_ticks() // 1000
    text = font.render(str(seconds),True,red)
    rect = text.get_rect()
    rect.center= (width//2,height//2)
    
    #surface.blit(text,rect)
    
    pygame.display.update()
    
    
            

