<<<<<<< HEAD
import random
import pygame
import time

pygame.init()

SCORE = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 400, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
#choosing path and setting up images
#c:\Users\Lenovo\Desktop\PP2\tsis8\1zad\\
path = r'c:\Users\Lenovo\Desktop\PP2\tsis8\1zad\\'
background_image = pygame.image.load(path + 'AnimatedStreet.png')
enemy_image = pygame.image.load(path + 'enemy.png')
player_image = pygame.image.load(path + 'player.png')
coin_image = pygame.image.load(path + 'coin.png')

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#setting up fonts
font = pygame.font.SysFont("Verdana", 30)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

clock = pygame.time.Clock()



#defining enemy
class Enemy():
    def __init__(self):
        self.speed = 10
        self.image = enemy_image
        self.rect = self.image.get_rect()
        #choosing random point in x-axis to spawn enemy
        random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
        self.rect.center = (random_width, 0)

    def update(self):
        global SCORE
        self.rect.y += self.speed // 1
        #cheking if enemy is outside of screen
        if self.rect.y > HEIGHT:
            SCORE += 1
            if self.speed < 20: 
                self.speed += 0.25 
            #choosing random point in x-axis to re-spawn enemy
            random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
            self.rect.center = (random_width, 0)


    def draw(self):
        SCREEN.blit(self.image, self.rect)

#defining Player
class Player():
    def __init__(self):
        self.speed = 5
        self.image = player_image
        self.rect = self.image.get_rect()
        #creating player in the middle
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)
    def update(self):
        pressed = pygame.key.get_pressed()
        #checking if player is still on screen before moving
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.x += self.speed
    def draw(self):
        SCREEN.blit(self.image, self.rect)

#adding sliding background
class Background():
    def __init__(self, start_y):
        self.image = background_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 + start_y)
    def draw(self):
        SCREEN.blit(self.image, self.rect)


    def update(self, speed):
        #if image is outside of screen moving to -HEIGHT by y-axis
        if self.rect.y >= HEIGHT + 10:
            self.rect.y = -HEIGHT - 10
        self.rect.y += speed
#defining coins
class Coin():
    def __init__(self, x, y):
        #getting initial coordinates
        self.x = x
        self.y = y
        
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self, speed):
        self.rect.y += speed

    
    def draw(self):
        SCREEN.blit(self.image, self.rect)

def add_coins(coins):
    for i in range(5):
        #choosing random point in x-axis
        random_width = random.randint(40, WIDTH - 40)
        coins.append(Coin(random_width, -(i) * HEIGHT * 0.15))
    return coins

def main():
    COLLECTED = 0
    enemy = Enemy()
    player = Player()
    background_1 = Background(0)
    background_2 = Background(-HEIGHT) #background_2 will follow background_1, that's why -HEIGHT 
    coins = []
    running = True

    while running:
        SCREEN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #checking if there is enough coins and adding if it's not
        if len(coins) < 2:
            add_coins(coins)

        #updating states of all entities exept coins
        background_1.update(enemy.speed // 3)
        background_2.update(enemy.speed // 3)
        player.update()
        enemy.update()
        #coins are drawn and updated below
        #drawing all entities exept coins
        background_1.draw()
        background_2.draw()
        player.draw()
        enemy.draw()

        #showing score and number of coins
        score = font_small.render("Your score: " + str(SCORE), True, BLACK)
        coins_text = font_small.render("Coins collected: " + str(COLLECTED), True, BLACK)
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(coins_text, (WIDTH // 2, 0))

        #checking for collision between player and enemy
        if player.rect.colliderect(enemy):
            SCREEN.blit(game_over, (30, 250))
            pygame.display.flip() #without this display won't update and won't show game_over
            time.sleep(1)
            running = False 

        i = 0
        while i < len(coins):
            #checking for collision between player and coin
            if player.rect.colliderect(coins[i]):
                COLLECTED += 1
                coins.pop(i)
                i -= 1
            #returning coin to its start position if it is outside of screen
            if coins[i].rect.y >= HEIGHT:
                coins[i].rect.y = -20
            i += 1

        #updating states of coins in list "coins", and drawing them
        for coin in coins:
            coin.update(enemy.speed // 3)
            coin.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
=======
import random
import pygame
import time

pygame.init()

SCORE = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 400, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
#choosing path and setting up images
#c:\Users\Lenovo\Desktop\PP2\tsis8\1zad\\
path = r'c:\Users\Lenovo\Desktop\PP2\tsis8\1zad\\'
background_image = pygame.image.load(path + 'AnimatedStreet.png')
enemy_image = pygame.image.load(path + 'enemy.png')
player_image = pygame.image.load(path + 'player.png')
coin_image = pygame.image.load(path + 'coin.png')

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#setting up fonts
font = pygame.font.SysFont("Verdana", 30)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

clock = pygame.time.Clock()



#defining enemy
class Enemy():
    def __init__(self):
        self.speed = 10
        self.image = enemy_image
        self.rect = self.image.get_rect()
        #choosing random point in x-axis to spawn enemy
        random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
        self.rect.center = (random_width, 0)

    def update(self):
        global SCORE
        self.rect.y += self.speed // 1
        #cheking if enemy is outside of screen
        if self.rect.y > HEIGHT:
            SCORE += 1
            if self.speed < 20: 
                self.speed += 0.25 
            #choosing random point in x-axis to re-spawn enemy
            random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
            self.rect.center = (random_width, 0)


    def draw(self):
        SCREEN.blit(self.image, self.rect)

#defining Player
class Player():
    def __init__(self):
        self.speed = 5
        self.image = player_image
        self.rect = self.image.get_rect()
        #creating player in the middle
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)
    def update(self):
        pressed = pygame.key.get_pressed()
        #checking if player is still on screen before moving
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.x += self.speed
    def draw(self):
        SCREEN.blit(self.image, self.rect)

#adding sliding background
class Background():
    def __init__(self, start_y):
        self.image = background_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 + start_y)
    def draw(self):
        SCREEN.blit(self.image, self.rect)


    def update(self, speed):
        #if image is outside of screen moving to -HEIGHT by y-axis
        if self.rect.y >= HEIGHT + 10:
            self.rect.y = -HEIGHT - 10
        self.rect.y += speed
#defining coins
class Coin():
    def __init__(self, x, y):
        #getting initial coordinates
        self.x = x
        self.y = y
        
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self, speed):
        self.rect.y += speed

    
    def draw(self):
        SCREEN.blit(self.image, self.rect)

def add_coins(coins):
    for i in range(5):
        #choosing random point in x-axis
        random_width = random.randint(40, WIDTH - 40)
        coins.append(Coin(random_width, -(i) * HEIGHT * 0.15))
    return coins

def main():
    COLLECTED = 0
    enemy = Enemy()
    player = Player()
    background_1 = Background(0)
    background_2 = Background(-HEIGHT) #background_2 will follow background_1, that's why -HEIGHT 
    coins = []
    running = True

    while running:
        SCREEN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #checking if there is enough coins and adding if it's not
        if len(coins) < 2:
            add_coins(coins)

        #updating states of all entities exept coins
        background_1.update(enemy.speed // 3)
        background_2.update(enemy.speed // 3)
        player.update()
        enemy.update()
        #coins are drawn and updated below
        #drawing all entities exept coins
        background_1.draw()
        background_2.draw()
        player.draw()
        enemy.draw()

        #showing score and number of coins
        score = font_small.render("Your score: " + str(SCORE), True, BLACK)
        coins_text = font_small.render("Coins collected: " + str(COLLECTED), True, BLACK)
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(coins_text, (WIDTH // 2, 0))

        #checking for collision between player and enemy
        if player.rect.colliderect(enemy):
            SCREEN.blit(game_over, (30, 250))
            pygame.display.flip() #without this display won't update and won't show game_over
            time.sleep(1)
            running = False 

        i = 0
        while i < len(coins):
            #checking for collision between player and coin
            if player.rect.colliderect(coins[i]):
                COLLECTED += 1
                coins.pop(i)
                i -= 1
            #returning coin to its start position if it is outside of screen
            if coins[i].rect.y >= HEIGHT:
                coins[i].rect.y = -20
            i += 1

        #updating states of coins in list "coins", and drawing them
        for coin in coins:
            coin.update(enemy.speed // 3)
            coin.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
>>>>>>> 9b5ac07d80476e4e1cc355b2632fe43998328617
    main()