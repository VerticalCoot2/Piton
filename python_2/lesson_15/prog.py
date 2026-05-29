import pygame
import os
from os import system as s

height = 500
width = 900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space fight")


WHITE = (255,255,255)

fps = 60
vel = 5
SpaceShipWidth = 80
SpaceShipHeight = 60

Yellow_SpaceShipImage = pygame.image.load('D:\LSC\Piton\python_2\lesson_15\Assets\spaceship_yellow.png')
Yellow_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Yellow_SpaceShipImage, (SpaceShipWidth, SpaceShipHeight)), 90)

red_SpaceShipImage = pygame.image.load('D:\LSC\Piton\python_2\lesson_15\Assets\spaceship_red.png')
Red_SpaceShip = pygame.transform.rotate(pygame.transform.scale(red_SpaceShipImage, (SpaceShipWidth, SpaceShipHeight)), 270)

def YellowCont(keys_pressed, yellow):
    if(keys_pressed[pygame.K_a]):
        yellow.x -= vel

    if(keys_pressed[pygame.K_d]):
        yellow.x += vel
    
    if(keys_pressed[pygame.K_w]):
        yellow.y -= vel

    if(keys_pressed[pygame.K_s]):
        yellow.y += vel

def RedCont(keys_pressed, red):
    if(keys_pressed[pygame.K_LEFT]):
        red.x -= vel

    if(keys_pressed[pygame.K_RIGHT]):
        red.x += vel
    
    if(keys_pressed[pygame.K_UP]):
        red.y -= vel

    if(keys_pressed[pygame.K_DOWN]):
        red.y += vel

def drawWindow(red, yellow):
    window.fill(WHITE)
    window.blit(Yellow_SpaceShip, (yellow.x, yellow.y))
    window.blit(Red_SpaceShip, (red.x, red.y))
    pygame.display.update()





def main():
    s("cls")
    red = pygame.Rect(700, 300, SpaceShipWidth, SpaceShipHeight)
    yellow = pygame.Rect(100, 300, SpaceShipWidth, SpaceShipHeight)

    clock = pygame.time.Clock()
    run = True
    
    while(run):
        clock.tick(fps)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
        keyPressed = pygame.key.get_pressed()
        RedCont(keyPressed, red)
        YellowCont(keyPressed, yellow)

        drawWindow(red, yellow)
    pygame.quit()
    



if __name__ == '__main__':
    main()