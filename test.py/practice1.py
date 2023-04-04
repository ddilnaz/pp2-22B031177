import pygame 
pygame.init()

WHITE = (255,255,255)
HEIGHT = 600
WIDTH = 400
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("ART")
x = HEIGHT // 2
y = WIDTH // 2
clock = pygame.time.Clock()
#RUN = True
speed = 10


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit()
        
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x>0: 
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    screen.fill(WHITE)
    pygame.draw.rect(screen , (0,255,0), (x  , y , 30,30) )
    pygame.display.update()
    clock.tick(60)
