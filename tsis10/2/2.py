from config import config
import psycopg2
import random
import pygame
import time
import sys
import csv


parameters = config()
conn = psycopg2.connect(**parameters)
cur = conn.cursor()

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 680
BLOCK_SIZE = 40
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT+20))

clock = pygame.time.Clock()
font  = pygame.font.SysFont(pygame.font.get_default_font(), 27)

RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = [0, 255, 0]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (128, 128, 128)

spawn_x = WIDTH // BLOCK_SIZE // 2
spawn_y = HEIGHT // BLOCK_SIZE // 2

save_image = pygame.image.load(r'C:\Users\Lenovo\Desktop\PP2\tsis10\2\save.png')

# defines point (cells) on screen
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# defines body and head of snake on points
class Snake():
    def __init__(self, body):
        # initiating body of snake
        self.body = body


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
    def check_bite(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True


    def check_collision(self, obstacles): # checks for collision with obstacles and borders
        # keeps snake in playing area
        if self.body[0].x >= WIDTH // BLOCK_SIZE:
            return True
        elif self.body[0].x < 0:
            return True
        elif self.body[0].y < 0:
            return True
        elif self.body[0].y >= HEIGHT // BLOCK_SIZE:
            return True
        
        # checks if snake's head collided with obstacle
        for block in obstacles.blocks:
            if block.x == self.body[0].x and block.y == self.body[0].y:
                return True
        return False

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


class Obstacle(): # defines obstacles
    def __init__(self, level):
        if level == 0 or level > 2:
            level = 1

        self.blocks = []
        path = r"C:\Users\Lenovo\Desktop\PP2\tsis10\2\maps\\"

        with open(f"{path}map ({level}).csv", "r") as file:
            reader = csv.reader(file)
            next(reader) # skipping header

            for row in reader:                
                x, y = int(row[0]), int(row[1])
                if x >= WIDTH // BLOCK_SIZE or y >= HEIGHT // BLOCK_SIZE:
                    continue
                elif x == spawn_x or y == spawn_y:
                    continue
                else:
                    self.blocks.append(Point(x, y))


    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(
                SCREEN,
                RED,
                pygame.Rect(
                    block.x * BLOCK_SIZE,
                    block.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )





class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = save_image
        self.rect = self.image.get_rect()


    def draw(self):    
        SCREEN.blit(self.image, (WIDTH-20, HEIGHT+2))




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




def log_in():
    login = input("Enter your login: ")
    if "--" in login:                       # preventing SQL-injection
        print("Error")
        return
    
    cur.execute(f"SELECT * FROM users WHERE login = '{login}'")
    user = cur.fetchone()

    if user is None:
        print("User not found, creating new user\nPress 'SAVE' to save your results")
        cur.execute(f"INSERT INTO users (login, level, max_score) VALUES ('{login}', 1, 0)")

        points = [[spawn_x, spawn_y]]
        cur.execute(f"INSERT INTO saved_state (id_login, snake_pos, current_score, dx, dy) VALUES ('{login}', ARRAY{points}, 0, 0, 0)")

        conn.commit()
        return 1, 0, 0, Snake([Point(spawn_x, spawn_y)]), 0, 0, login
    
    else:
        level, max_score = user[1], user[2]
        print(f"Welcome back {login}!")
        cur.execute(f"SELECT * FROM saved_state WHERE id_login = '{login}'")
        saved = cur.fetchone()

        points = []
        saved_pos = saved[1]
        for pos in saved_pos:
            points.append(Point(pos[0], pos[1]))
        
        score, dx, dy = saved[2], saved[3], saved[4]

        return level, max_score, score, Snake(points), dx, dy, login




def save_results(login, level, max_score, score, snake, dx, dy):
    max_score = max(max_score, score)
    cur.execute(f"UPDATE users SET level = {level} WHERE login = '{login}'")
    cur.execute(f"UPDATE users SET max_score = {max_score} WHERE login = '{login}'")
    cur.execute(f"UPDATE saved_state SET current_score = {score} WHERE id_login = '{login}'")
    cur.execute(f"UPDATE saved_state SET dx = {dx} WHERE id_login = '{login}'")
    cur.execute(f"UPDATE saved_state SET dy = {dy} WHERE id_login = '{login}'")
    
    snake_pos = []
    for block in snake.body:
        snake_pos.append([block.x, block.y])
    cur.execute(f"UPDATE saved_state SET snake_pos = ARRAY{snake_pos} WHERE id_login = '{login}'")
    conn.commit()




def game_over():
    cur.close()
    conn.close()
    print("game over")
    sys.exit()




def main():
    spawn_time = time.perf_counter()
    to_append = 0
    running = True
    paused = False
    new_level = False   # for new level message

    level, max_score, score, snake, dx, dy, login = log_in()

    food  = Food(5, 5)
    obstacles = Obstacle(level)
    save_button = Button()
    time.sleep(1) # just to be ready
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
                    paused = not paused
            
            if event.type == pygame.MOUSEBUTTONDOWN and not new_level:
                save_button.rect.collidepoint(pygame.mouse.get_pos())
                save_results(login, level, max_score, score, snake, dx, dy)
                time.sleep(3)
                print("Saved!")

        if paused:
            continue

        if len(snake.body) > 10 and not new_level:
            new_level = True
            print("New level available, it will swith when you restart the game")
            save_results(login, level+1, max(max_score, score), 0, Snake([Point(spawn_x, spawn_y)]), 0, 0)
        snake.move(dx, dy)
        # appending snake's body
        if snake.check_bite(food):
            spawn_time = time.perf_counter()
            score += 1
            to_append += food.weight
            food.generate_new(snake.body)
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            to_append -= 1
        elif to_append > 0: # if there is any need to add new rectangles to snakess body
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            to_append -= 1
        
        if snake.check_collision(obstacles):
            game_over()

        # re-spawn food when it's expired
        if time.perf_counter() - spawn_time > 5:
            spawn_time = time.perf_counter()
            food.generate_new(snake.body)

        max_score_font = font.render('Max score: ' + str(max_score), True, (255, 255, 255))
        score_font = font.render('Score: ' + str(score), True, (255, 255, 255))
        level_font = font.render('Level: ' + str(level), True, (255, 255, 255))

        SCREEN.fill(BLACK)
        SCREEN.blit(score_font, (0, HEIGHT))
        SCREEN.blit(max_score_font, (WIDTH * 2 // 3, HEIGHT))
        SCREEN.blit(level_font, (WIDTH // 3, HEIGHT))

        snake.draw()
        food.draw()
        obstacles.draw()
        save_button.draw()
        draw_grid()

        pygame.display.flip()
        clock.tick(score // 5 * 2 + 5)


if __name__ == '__main__':
    main()
    cur.close()
    conn.close()