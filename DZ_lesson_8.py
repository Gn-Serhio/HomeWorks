##  Задача 1 - Создать текстовый файл, в котором будут хранится данные о людях (1 строка, один объект). Нужно из файла сделать лист объкетов

import os
f = open('person.txt', 'r', encoding='utf-8')
class Peoples:
    def __init__(self, name, lastname, profession):
        self.__name = name
        self.__lastname = lastname
        self.__profession = profession

    def say_hello(self):
        print(f'hello my name is {self.__name} {self.__lastname}, I am worf {self.__profession}')

    def info(self):
        print(f'name = {self.__name}, lastname = {self.__lastname}, profession = {self.__profession}')
li = []
for i in f:
    i = i.replace('\n', '')
    s = i.split()
    li.append(s)
peoples = Peoples(li[0][0], li[0][1], li[0][2])
peoples1 = Peoples(li[1][0], li[1][1], li[1][2])
peoples2 = Peoples(li[2][0], li[2][1], li[2][2])
peoples.info()


# #  Задача 2 - сделать тоже самое для exel таблицы

import openpyxl
import os
file = openpyxl.open('peoples.xlsx', read_only=True)
sheet = file.active

class Peoples:
    def __init__(self, name, lastname, profession):
        self.__name = name
        self.__lastname = lastname
        self.__profession = profession

    def say_about(self):
        print(f'Меня зовут {self.__name} {self.__lastname}, моя профессия {self.__profession}')

    def info(self):
        print(f'name = {self.__name}, lastname = {self.__lastname}, profession = {self.__profession}')

li = []
for row in range(1,4):
    li.append([])
    for column in range(3):
        li[row-1].append(sheet[row][column].value)

peoples = Peoples(li[0][0], li[0][1], li[0][2])
peoples1 = Peoples(li[1][0], li[1][1], li[1][2])
peoples2 = Peoples(li[2][0], li[2][1], li[2][2])
peoples.info()
peoples1.info()
peoples2.info()
peoples.say_about()
peoples1.say_about()
peoples2.say_about()

## Задача 3 - Создать класс круг, принимать в конструктор радиус и на основе него расчитывать длинну окружности и площадь круга (делать в конструкторе)

import math
class Circle:
    def __init__(self, radius):
            self.__radius = radius

    def length(self):
        l = 2 * math.pi * self.__radius
        print('Длина окружности равна =', l)
    def square(self):
        s = 2 * math.pi * self.__radius**2
        print('Площадь круга равна =', s)

circle = Circle(int(input('Введите радиус окружности ---->  ')))
circle.length()
circle.square()

## Задача 4 - Создать класс треугольник, в который принимаем длинны сторон. Записать в поле тип либо прямоугольный... и определить в поле характеристику угла острый/тупой

import math
class Triangle:
    def __init__(self, side_a, side_b, side_c):
            self.__side_a = side_a
            self.__side_b = side_b
            self.__side_c = side_c

    def type(self):
        if self.__side_a + self.__side_b > self.__side_c and self.__side_a + self.__side_c > self.__side_b and \
            self.__side_b + self.__side_c > self.__side_a:
            if self.__side_a == self.__side_b and self.__side_a == self.__side_c:
                print('Треугольник равносторонний')
            if self.__side_a == self.__side_b and self.__side_a != self.__side_c or \
                self.__side_a == self.__side_c and self.__side_a != self.__side_b or\
                self.__side_b == self.__side_c and self.__side_a != self.__side_c:
                print('Треугольник равнобедренный')
            if self.__side_a != self.__side_b and self.__side_b != self.__side_c and self.__side_a != self.__side_c:
                print('Треугольник разносторонний')
        else:
            print("Треугольник не существует")

    def corner(self):
        ab = (math.acos((self.__side_a**2 + self.__side_b**2 - self.__side_c**2) / (2 * self.__side_a * self.__side_b))) * 180 / math.pi
        bc = (math.acos((self.__side_b**2 + self.__side_c**2 - self.__side_a**2) / (2 * self.__side_c * self.__side_b))) * 180 / math.pi
        ca = (math.acos((self.__side_a**2 + self.__side_c**2 - self.__side_b**2) / (2 * self.__side_c * self.__side_a))) * 180 / math.pi
        if 0 < ab < 90:
            print('Угол АB - ОСТРЫЙ')
        elif ab > 90:
            print('Угол АB - ТУПОЙ')
        else:
            print('Угол АB - Прямой')
        if 0 < bc < 90:
            print('Угол BC - ОСТРЫЙ')
        elif bc > 90:
            print('Угол BC - ТУПОЙ')
        else:
            print('Угол BC - Прямой')
        if 0 < ca < 90:
            print('Угол AC - ОСТРЫЙ')
        elif ca > 90:
            print('Угол AC - ТУПОЙ')
        else:
            print('Угол AC - Прямой')

triangle = Triangle(int(input('Введите сторону A' + '\n')), int(input('Введите сторону B' + '\n')), int(input('Введите сторону C' + '\n')))
triangle.type()
triangle.corner()