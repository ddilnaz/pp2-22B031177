import pygame 
pygame.init()

H = 600 
W = 400
WHITE = (255,255,255)
sc = pygame.display.set_mode((H,W))
pygame.display.set_caption("ART")
run = True
clock = pygame.time.Clock()

pygame.draw.rect(sc , (255, 255 ,255) ,( H//2 , W//2 , 50 , 100), 5)
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



sc.fill(WHITE)
screen.display.update()
clock.tick(60)

