import pygame

import math

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GRAY = pygame.Color(127, 127, 127)

class GameObject:
    def draw(self):
        raise NotImplementedError
    def handle(self):
        raise NotImplementedError


class Button(pygame.sprite.Sprite):
    def __init__(self, points, width=0, color=GRAY):
        super().__init__()
        self.points = points
        self.width  = width
        self.color = color
        self.rect = pygame.draw.polygon(SCREEN, self.color, self.points, self.width)
    def draw(self):    
        pygame.draw.polygon(SCREEN, self.color, self.points, self.width)

class Pen(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):
        self.thickness = thickness
        self.color = color
        self.points = [] 

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                self.color,
                start_pos=point, 
                end_pos=self.points[idx + 1],
                width=self.thickness,
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)
class Rectangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):
        self.thickness = thickness
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        #start positions
        x1 = min(self.start_pos[0], self.end_pos[0])
        y1 = min(self.start_pos[1], self.end_pos[1])
        #end positions
        x2 = max(self.start_pos[0], self.end_pos[0])
        y2 = max(self.start_pos[1], self.end_pos[1])

        #рисует чет-и
        pygame.draw.rect(SCREEN, self.color, (x1, y1, x2 - x1, y2 - y1), width=self.thickness)

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class RightTriangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):
        self.thickness = thickness
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos
    def draw(self):
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos

        side_len = x2-x1                      #вычисляем длину 
        h = math.pow(side_len**2 * 0.75, 0.5) #вычисляем высоту

        if side_len < 0: h *= -1              #triangle
        
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y1)
        vertex_3 = (x1 + side_len/2, y1 - h)
        vertices = [vertex_1, vertex_2, vertex_3]
        #рисуем правильный тр-к
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)
    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class EquilateralTriangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):
        self.thickness = thickness
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos
        w = (x2 - x1) *2

        #вершина
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y2)
        vertex_3 = (x2-w, y2)
        vertices = [vertex_1, vertex_2, vertex_3]

        #равнобедерный триангл
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)
    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Rhombus(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):
        self.thickness = thickness
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos
    def draw(self):
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos

        side_len = math.pow((x2-x1)**2 + (y2-y1)**2, 0.5)
        #вершина
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y2)
        vertex_3 = (x2 + side_len, y2)
        vertex_4 = (x1 + side_len, y1)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4]
        #ромбик
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)
    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

def main():
    Points_P   = [(28, 10), (12, 50)]
    Points_S   = [(50, 10), (90, 10), (90, 50), (50, 50)]
    Points_RT  = [(135, 10), (170, 50), (100, 50)]             
    Points_EqT = [(195, 10), (210, 50), (180, 50)]           
    Points_rh  = [(240, 10), (260, 30), (240, 50), (220, 30)]

    switch_pen       = Button(Points_P, 5)
    switch_square    = Button(Points_S)
    switch_triangleR = Button(Points_RT)
    switch_triangleW = Button(Points_EqT)
    switch_rhombus   = Button(Points_rh)
    buttons = [switch_pen,switch_square,switch_triangleR,switch_triangleW,switch_rhombus,]
    current_shape = 'pen'
    objects = []
    active_obj = None
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons_dict = {
                    switch_pen       :'pen',
                    switch_square    :'square',
                    switch_triangleR :'rightT',
                    switch_triangleW :'wrongT',
                    switch_rhombus   :'rhombus',
                }
                for key in buttons_dict.keys():
                    if key.rect.collidepoint(pygame.mouse.get_pos()):
                        current_shape = buttons_dict[key]
                else:
                    shapes = {
                        'pen'    : Pen(start_pos=event.pos), 
                        'square' : Rectangle(start_pos=event.pos),
                        'rightT' : RightTriangle(start_pos=event.pos),
                        'wrongT' : EquilateralTriangle(start_pos=event.pos),
                        'rhombus': Rhombus(start_pos=event.pos),
                        }
                    active_obj = shapes[current_shape]

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.handle(mouse_pos=pygame.mouse.get_pos())
                active_obj.draw()

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None

        for button in buttons:
            button.draw()
        for obj in objects:
            obj.draw()

        clock.tick(30)
        pygame.display.flip()

if __name__ == '__main__':
    main()