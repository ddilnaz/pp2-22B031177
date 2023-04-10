import random
import pygame
import time

pygame.init()

SCORE = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 400, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
#c:\Users\Lenovo\Desktop\PP2\tsis9\1zad
path = r'C:\Users\Lenovo\Desktop\PP2\tsis9\1zad\\'
background_image = pygame.image.load(path + 'koshe.png')
enemy_image      = pygame.image.load(path + 'vrag.png')
player_image     = pygame.image.load(path + 'igrok.png')
coin_image_L1    = pygame.image.load(path + 'money1.png')
coin_image_L2    = pygame.image.load(path + 'money2.png')
coin_image_L3    = pygame.image.load(path + 'money3.png')

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

font = pygame.font.SysFont("Verdana", 30)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
clock = pygame.time.Clock()

class Enemy():
    def __init__(self):
        self.speed = 10
        self.image = enemy_image
        self.rect = self.image.get_rect()
        #рандомный пойнт для врага по иксу 
        random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
        self.rect.center = (random_width, 0)

    def update(self):
        global SCORE
        self.rect.y += self.speed // 1

        #проверяем не вышел ли враг за границу
        if self.rect.y > HEIGHT:
            SCORE += 1
            random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
            self.rect.center = (random_width, 0)


    def draw(self):
        SCREEN.blit(self.image, self.rect)

class Player():
    def __init__(self):
        self.speed = 5
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.x += self.speed
    
    def draw(self):
        SCREEN.blit(self.image, self.rect)

class Background():
    def __init__(self, start_y):
        self.image = background_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 + start_y)

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self, speed):
        if self.rect.y >= HEIGHT + 10:
            self.rect.y = -HEIGHT - 10
        self.rect.y += speed

class Coin():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        image_dict = {
            1 : coin_image_L1,
            2 : coin_image_L2,
            3 : coin_image_L3,
        }
        self.image = image_dict[num]
        self.weight = num
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, speed):
        self.rect.y += speed

    def draw(self):
        SCREEN.blit(self.image, self.rect)

def add_coins(coins):
    for i in range(4):
        random_width = random.randint(40, WIDTH - 40)
        num = random.randint(1, 3)
        coins.append(Coin(random_width, -(i) * HEIGHT * 0.15, num))
    return coins

def main():
    COLLECTED = 0
    CoeficientN = 10
    enemy = Enemy()
    player = Player()
    background_1 = Background(0)
    background_2 = Background(-HEIGHT)  
    coins = []
    running = True

    while running:
        SCREEN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if len(coins) <= 1:
            add_coins(coins)
        background_1.update(enemy.speed // 3)
        background_2.update(enemy.speed // 3)
        player.update()
        enemy.update()
        background_1.draw()
        background_2.draw()
        player.draw()
        enemy.draw()

        score = font_small.render("Your score: " + str(SCORE), True, BLACK)
        coins_text = font_small.render("Coins collected: " + str(COLLECTED), True, BLACK)
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(coins_text, (WIDTH // 2, 0))

        if player.rect.colliderect(enemy):
            SCREEN.blit(game_over, (30, 250))
            pygame.display.flip() 
            time.sleep(2)
            running = False 

        i = 0
        while i < len(coins):
            if player.rect.colliderect(coins[i]):
                COLLECTED += coins[i].weight
                enemy.speed += COLLECTED // CoeficientN * 0.25
                coins.pop(i)
                i -= 1
            if coins[i].rect.y >= HEIGHT + 20:
                coins[i].rect.y = -20
            i += 1

        for coin in coins:
            coin.update(enemy.speed // 3)
            coin.draw()
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()