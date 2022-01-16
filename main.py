import random
import copy
import time

'''
Описание класса клетки (единицы игрового поля). Состояние (condition) - живёт ли в ней существо (1 - да, 0 - нет).
Координаты введены для отслеживания соседей клетки.
'''


class Cell:
    __condition = 0
    __x, __y = 0, 0

    def __init__(self, condition, x, y):
        self.condition = condition
        self.x, self.y = x, y

    def count_neighbours(self):
        res = 0
        for i, j in get_xy(self.x, self.y):
            if isAlive(i, j):
                res += 1

        return res

    def get_condition(self):
        return self.condition

    def get_str_condition(self):
        if self.condition == 0:
            return '0'
        else:
            return '1'

    def set_condition(self, condition):
        self.condition = condition


'''
Описание класса поля. Задаются его размеры, оно заполнено клетками, в которые случайным образом заселяются живые
существа. Поле незамкнуто (то есть бесконечно. Можно сказать, что к полю со всех сторон присоединены его копии).
'''


class Field:
    __sizeX = 0
    __sizeY = 0
    cells = []

    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.cells = []
        self.cells = [[Cell(random.randint(0, 1), i, j) for i in range(sizeX)] for j in range(sizeY)]

    def get_sizeX(self):
        return self.sizeX

    def get_sizeY(self):
        return self.sizeY

    def rotation(self):
        next_cells = [[Cell(0, i, j) for i in range(self.sizeX)] for j in range(self.sizeY)]
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                if isAlive(x, y):
                    if 2 <= self.cells[y][x].count_neighbours() <= 3:
                        next_cells[y][x].set_condition(1)
                    else:
                        next_cells[y][x].set_condition(0)
                else:
                    if self.cells[y][x].count_neighbours() == 3:
                        next_cells[y][x].set_condition(1)
                    else:
                        next_cells[y][x].set_condition(0)

        self.cells = copy.deepcopy(next_cells)

    def draw(self):
        for y in range(self.sizeY):
            s = ''
            for x in range(self.sizeX):
                s += self.cells[y][x].get_str_condition()
            print(s)
        print('_' * self.sizeX)

    def get_cell(self, x, y):
        return self.cells[y][x]


'''
Функция для определения состояния клетки и функция для получения координат соседей клетки. 
'''


def isAlive(x, y):
    return field.get_cell(x, y).get_condition() == 1


def get_xy(x, y):
    for dx, dy in ((0, 1),
                   (1, 1),
                   (1, 0),
                   (1, -1),
                   (0, -1),
                   (-1, -1),
                   (-1, 0),
                   (-1, 1)):
        yield (x + dx) % field.get_sizeX(), (y + dy) % field.get_sizeY()


field = Field(25, 15)

while True:
    field.draw()
    field.rotation()
    time.sleep(0.4)
