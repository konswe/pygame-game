from operator import truediv
import pygame

pygame.display.set_caption('game')

(width, height) = (700, 700)
background_color = (172, 79, 232)
screen = pygame.display.set_mode((width, height))

characterImg = pygame.image.load('images.png')
characterImg = pygame. transform. scale(characterImg, (20, 20))

characterX=300
characterY=300

def character():
    screen.blit(characterImg, (characterX, characterY))    

runs = True

while runs:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runs = False

    
    character()

    pygame.display.update()




    