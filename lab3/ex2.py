import pygame
from pygame.draw import *

pygame.init()

FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
grey = 	(190, 190, 190)
lblue = (128, 166, 255)
dblue = (0, 0, 139)
light_grey = (170, 170, 170)
brown = (84, 50, 3)
dbrown = (26, 15, 1)
beige = (196, 174, 145)
pi = 3.14
screen.fill(grey)
rect(screen,'white', (0,300, 600, 300))
def igloo(x,y, size):
    ellipse(screen, grey, (x, y, 300//size, 225//size))
    rect(screen, 'white', (x, y+112//size, 300//size, 112//size))
    arc(screen, 'black', (x, y, 300 // size, 225 // size), 0, pi, 4 // size)
    line(screen, 'black', (x, y + 112//size), (x + 300//size, y + 112//size), 1)
    line(screen, 'black', (x + 13//size, y + 75//size), (x + 287//size, y + 75//size), 1)
    xi = 20//size
    for i in range(5):
        line(screen, 'black', (x+xi//size, y + 112//size), (x+xi//size, y + 75//size ), 1)
        xi += 60
    line(screen, 'black', (x + 34//size, y + 45//size), (x + 267//size, y + 45//size), 1)
    xi = 30//size
    for i in range (4):
        line(screen, 'black', (x + 34//size + xi//size, y + 75//size), (x + 34//size + xi//size, y + 45//size), 1)
        xi += 60
    line(screen, 'black', (x + 62//size, y + 20//size), (x + 237//size, y + 20//size), 1)
    xi = 30//size
    for i in range(3):
        line(screen, 'black', (x + 62//size + xi//size, y + 45//size), (x + 62//size + xi//size,y + 20//size ), 1)
        xi += 60
    line(screen, 'black', (x + 150//size, y), (x+ 180//size, y + 20//size), 1)

def cat(x, y):
    ellipse(screen,grey, (x, y, 180, 30))
    paws = pygame.Surface((15,80))
    paws.set_colorkey('black')
    ellipse(paws, grey, (0,0, 15, 80))
    paws = pygame.transform.rotate(paws, -70)
    screen.blit(paws, (x-10, y+20))
    paws = pygame.transform.rotate(paws, -10)
    screen.blit(paws, (x-40, y-5))
    paws = pygame.transform.rotate(paws, -35)
    screen.blit(paws, (x + 85,y-15))
    screen.blit(paws, (x + 140,y-15))
    tail = pygame.Surface((15,100))
    tail.set_colorkey('black')
    ellipse(tail, grey, (0,0, 15, 100))
    tail = pygame.transform.rotate(tail, -60)
    screen.blit(tail, (x+170, y - 40))
    fish = pygame.Surface((100, 50))
    polygon(fish, lblue, [(0,20), (0,40), (40, 30)])
    ellipse(fish, lblue, (40, 15, 60, 30))
    circle(fish, 'blue', (80, 30), 6)
    polygon(fish, 'red', [(80, 45), (60, 45), (55, 50), (80, 50)])
    polygon(fish, 'red', [(85, 16), (65, 16), (45, 3), (85,3)])
    fish = pygame.transform.scale(fish, (50,25))
    fish = pygame.transform.rotate(fish, 150)
    fish.set_colorkey('black')
    screen.blit(fish, (x, y - 10))
    head = pygame.Surface((70, 40))
    head.set_colorkey('black')
    ellipse(head, grey,(10,5, 50, 30))
    head = pygame.transform.rotate(head, 7)
    teeth = pygame.Surface((10,10))
    polygon(teeth, 'white', [(0,0),(0,10), (10,5)])
    teeth.set_colorkey('black')
    teeth = pygame.transform.rotate(teeth, -130)
    head.blit(teeth, (14,28))
    head.blit(teeth, (5,17))
    circle(head, 'white', (45, 24) , 5 )
    circle(head, 'white', (38, 10) , 5 )
    circle(head, 'blue', (38, 10) , 2 )
    circle(head, 'blue', (45, 24) , 2 )
    ears = pygame.Surface((10,10))
    polygon(ears, grey, [(0,10), (10,10), (5,0)])
    ears.set_colorkey('black')
    ears = pygame.transform.rotate(ears, 40)
    ears2 = pygame.transform.rotate(ears, 42)
    head.blit(ears, (53,10))
    head.blit(ears2, (42, 0))
    circle(head, dblue, (30, 20), 2)
    screen.blit(head, (x+10 ,y-25))
def esk (x, y, size, flp):
    eskimos = pygame.Surface((250,300))
    eskimos.fill('blue')
    circle(eskimos, beige, (125, 60), 50)
    ellipse(eskimos,brown, (75 , 75 , 100, 200) )
    rect(eskimos, 'blue', (50, 170, 250, 150))
    ellipse(eskimos, brown, (90, 145, 25,50))
    ellipse(eskimos, brown, (70, 180,40, 20))
    ellipse(eskimos, brown, (135, 145, 25, 50))
    ellipse(eskimos, brown, (140, 180, 40, 20))
    rect(eskimos, dbrown, (75,159, 100, 10))
    circle(eskimos, (84, 50, 50), (125, 60), 40)
    circle(eskimos, beige, (125, 60), 30)
    rect(eskimos, dbrown, (115,  90, 20, 70))
    line(eskimos, 'black', (100, 50), (115, 55),2)
    line(eskimos, 'black', (150, 50), (130, 55),2)
    arc(eskimos, 'black', (110, 70,30, 10), 0, pi, 2)
    ellipse(eskimos, brown, (40, 100, 60,20))
    line(eskimos, 'black', (40, 40), (60, 170))
    hand = pygame.Surface((60,20))
    ellipse(hand, brown, (0,0,60,20))
    hand.set_colorkey('black')
    hand = pygame.transform.rotate(hand, -30)
    eskimos.blit(hand, (140,90))
    eskimos.set_colorkey('blue')
    eskimos = pygame.transform.flip(eskimos, flp, False)
    eskimos = pygame.transform.scale(eskimos, (250/size, 300/size))
    screen.blit(eskimos, (x,y))


igloo(50,250, 1)
cat(100, 500)
esk(320, 250, 1, False)
pygame.display.update()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()