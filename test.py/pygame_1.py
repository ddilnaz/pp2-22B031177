import pygame

pygame.init()
HEIGHT , WIDTH = 500 , 500
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("DIKON")

running = True
while running:
    screen.fill(0,255,0)
        for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
        if event.type == pygame.KEYDOWN:
            print ('here')