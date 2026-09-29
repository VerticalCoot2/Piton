import pygame
import os
from os import system as s

pygame.font.init()
pygame.mixer.init()

height = 500
width = 900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space fight")


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(width // 2 -5, 0, 10, height)

BULLET_HIT_SOUND = pygame.mixer.Sounds("D:\LSC\Piton\python_2\lesson_15-16-17\Assets\explosion.wav")
BULLET_FIRE_SOUND = pygame.mixer.Sound("D:\LSC\Piton\python_2\lesson_15-16-17\Assets\laser.wav")

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

fps = 60
vel = 5
bulletVel = 7
maxBullets = 3
SpaceShipWidth = 80
SpaceShipHeight = 60

YellowHit = pygame.USEREVENT + 1
RedHit = pygame.USEREVENT + 2



Yellow_SpaceShipImage = pygame.image.load('D:\LSC\Piton\python_2\lesson_15-16-17\Assets\spaceship_yellow.png')
Yellow_SpaceShip = pygame.transform.rotate(pygame.transform.scale(Yellow_SpaceShipImage, (SpaceShipWidth, SpaceShipHeight)), 90)

red_SpaceShipImage = pygame.image.load('D:\LSC\Piton\python_2\lesson_15-16-17\Assets\spaceship_red.png')
Red_SpaceShip = pygame.transform.rotate(pygame.transform.scale(red_SpaceShipImage, (SpaceShipWidth, SpaceShipHeight)), 270)

Space = pygame.transform.scale(pygame.image.load('D:\LSC\Piton\python_2\lesson_15-16-17\Assets\space.png'), (width, height))


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

def drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    window.blit(Space, 0, 0)
    # window.fill(WHITE)
    pygame.draw.rect(window, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), True, WHITE)

    window.blit(red_health_text, (width - red_health_text.get_width()-10,10))
    window.blit(yellow_health_text, yellow_health_text, (10,10))

    window.blit(Yellow_SpaceShip, (yellow.x, yellow.y))
    window.blit(Red_SpaceShip, (red.x, red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(window, red, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(window, yellow, bullet)

    pygame.display.update()

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bulletVel

        if red.colliderect(bullet):
            pygame.event.pos(pygame.event.Event(RedHit))
            yellow_bullets.remove(bullet)
        elif bullet.x > width:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets





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