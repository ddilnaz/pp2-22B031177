import random
import pygame
import time
import sys

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 680
BLOCK_SIZE = 40
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT+20))

clock = pygame.time.Clock()
font = pygame.font.SysFont(pygame.font.get_default_font(), 27)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = [0, 255, 0]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# defines point (cells) on screen
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y




# defines body and head of snake on points
class Snake():
    def __init__(self):
        # initiating head
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]


    # draws body and head
    def draw(self):
        head = self.body[0]
        
        # draws head
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

        # draws body
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )


    # moves body after head
    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y

        self.body[0].x += dx
        self.body[0].y += dy

        # finishes the game when snake bites itself
        for idx in range(len(self.body) - 1, 0, -1):
            if self.body[idx].x == self.body[0].x and self.body[idx].y == self.body[0].y:
                game_over()

        # keeps snake in playing area
        if self.body[0].x >= WIDTH // BLOCK_SIZE:
            game_over()
        elif self.body[0].x < 0:
            game_over()
        elif self.body[0].y < 0:
            game_over()
        elif self.body[0].y >= HEIGHT // BLOCK_SIZE:
            game_over()


    # checks if food is eaten
    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True




class Food: # defines foods
    def __init__(self, x, y):
        self.color = GREEN
        self.weight = 1
        self.location = Point(x, y)

    
    def draw(self): #draws food rectangles
        pygame.draw.rect(
            SCREEN,
            self.color,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
    

    def generate_new(self, snake_body):
        self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        # choosing weight
        self.weight = random.randint(1, 3)
        # giving different color depending on weight
        self.color[0] = 200 - (self.weight - 1) * 100
        self.color[2] = 200 - (self.weight - 1) * 100
        # checks if food fell on snake's body, if true: generates again and checks from the beginning 
        for idx in range(len(snake_body) - 1, 0, -1):
            if self.location.x == snake_body[idx].x and self.location.y == snake_body[idx].y:
                self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                idx = len(snake_body) - 1




def draw_grid():
    # draw cells
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

    # draw borders
    pygame.draw.line(SCREEN, RED, start_pos=(0, HEIGHT-1), end_pos=(WIDTH-1, HEIGHT-1), width=1)  #bottom border
    pygame.draw.line(SCREEN, RED, start_pos=(0, 0), end_pos=(0, HEIGHT), width=1)   #left border
    pygame.draw.line(SCREEN, RED, start_pos=(WIDTH-1, 0), end_pos=(WIDTH-1, HEIGHT-1), width=1)   #right border
    pygame.draw.line(SCREEN, RED, start_pos=(0, 0), end_pos=(WIDTH, 0), width=1)    #top border




def game_over():
    print("game over")
    sys.exit()




def main():

    running = True
    spawn_time = time.perf_counter()
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0
    score = 0
    level = 0
    to_append = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # forbids going backwards   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy != 1:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and dy != -1:
                    dx, dy = 0, 1
                elif event.key == pygame.K_RIGHT and dx != -1:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT and dx != 1:
                    dx, dy = -1, 0
                elif event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_p:
                    time.sleep(10)


        snake.move(dx, dy)

        # appending snake's body
        if snake.check_collision(food):
            spawn_time = time.perf_counter()
            score += 1
            level = score // 3
            to_append += food.weight
            food.generate_new(snake.body)
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            to_append -= 1
        elif to_append > 0: # if there is any need to add new rectangles to snakess body
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            to_append -= 1

        # re-spawn food when it's expired
        if time.perf_counter() - spawn_time > 5:
            spawn_time = time.perf_counter()
            food.generate_new(snake.body)

        score_font = font.render('Score: ' + str(score), True, (255, 255, 255))
        level_font = font.render('Level: ' + str(level), True, (255, 255, 255))

        SCREEN.fill(BLACK)
        SCREEN.blit(score_font, (0, HEIGHT))
        SCREEN.blit(level_font, (WIDTH // 2, HEIGHT))

        snake.draw()
        food.draw()
        draw_grid()

        pygame.display.flip()
        clock.tick(2 * level + 5)


if __name__ == '__main__':
    main()