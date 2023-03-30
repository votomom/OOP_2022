import pygame
from pygame.draw import *

pygame.init()

FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
screen.fill('white')

circle(screen,'yellow', (200, 200), 100)
circle(screen,'red', (160, 170), 20)
circle(screen,'black', (160, 170), 10)
circle(screen,'red', (240, 170), 15)
circle(screen,'black', (240, 170), 7)
line(screen, 'black', (110,120 ), (180, 155), 8)
line(screen, 'black', (290,130 ), (220, 156), 8)
rect(screen, 'black', (150,240, 100, 20))


pygame.display.update()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()