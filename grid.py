import numpy
import pygame
import random

class layout:
    def __init__(self, width, height, rate, thickness):
        self.rate = rate #30
        self.row = int(width / rate)
        self.col = int(height/rate)
        #размер формы
        self.size = (self.row, self.col)
        self.array = numpy.ndarray(shape=(self.size))
        self.thickness = thickness

    def random(self):
        #закрашивание клеток в начале игры
        for x in range(self.row): #цикл количество чисел от 0 до row
            for y in range(self.col):#цикл количество чисел от 0 до col
                self.array[x][y] = random.randint(0,1) # случайное число 0 или 1

    def conway(self, off, on, surface, pause):
        for x in range(self.row): #цикл количество чисел от 0 до row
            for y in range(self.col): #цикл количество чисел от 0 до col
                y_pos = y * self.rate
                x_pos = x * self.rate
                if self.array[x][y] == 1:
                    pygame.draw.rect(surface, on, [x_pos, y_pos, self.rate-self.thickness, self.rate-self.thickness]) #"Живые" клетки
                else:
                    pygame.draw.rect(surface, off, [x_pos, y_pos, self.rate-self.thickness, self.rate-self.thickness]) # "Мертвые" клетки

#основной алгоритм игры
        next = numpy.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.row):
                for y in range(self.col):
                    state = self.array[x][y]
                    neighbours = self.get_neighbours( x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.array = next

    #ЛКМ закрасить клетку
    def leftmouse(self, x, y):
        _x = x//self.rate
        _y = y//self.rate

        if self.array[_x][_y] != None:
            self.array[_x][_y] = 1

    #ПКМ удалить клетку
    def rightmouse(self, x, y):
        _x = x//self.rate
        _y = y//self.rate

        if self.array[_x][_y] != None:
            self.array[_x][_y] = 0


    def get_neighbours(self, x, y): #соседние клетки
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.row) % self.row
                y_edge = (y+m+self.col) % self.col
                total += self.array[x_edge][y_edge]

        total -= self.array[x][y]
        return total
