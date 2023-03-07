## Задача 1 - Написать функцию для ввода листа с клавиатуры

def enter_list(word):
    return word

print(enter_list(input('Введите элементы списка через "ПРОБЕЛ" \n').split(' ')))


## Задача 2 - Написать функцию для ввода словаря с клавиатуры

def di(k,v):
    dic[k] = v
    return dic

dic = {}
key = input('Введите ключ \n')
value = input('Введите величину \n')
while key != 'stop' or value == 'stop':
    print(di(key, value))
    key = input('Введите ключ \n')
    value = input('Введите величину \n')
print(dic)

## Задача 3 - Написать функцию для поиска уникальных элементов в листе (которые встречаются один раз в нем)

def li(l):
    for i in l:
        count = l.count(i)
        if count == 1:
            print(i)

list = [1, 2, 3, 4, 2, 4, 1, 6]
li(list)

## Задача 4 - Проверка IP-адреса

def ip(str):
    for i in row:
        if 0 <= i <= 255 and len(row) == 4:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print('YES')
    else:
        print('NO')
try:
    row = [int(i) for i in input('Введите IP-адрес \n').split('.')]
    flag = True
    ip(row)
except ValueError:
    print('IP-адрес введен неправильно \n')

## Задача 5 - матрица n*n (n <= 100), главная диагональ 0, прилегающие 1, следующие 2 и т.д.

n = int(input())
matrix = [[0]*n for i in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = abs(j-i)
for i in matrix:
    print(*i)

## Задача 5 - в конотеатре n рядов и m мест (<=20).....

num = [int(a) for a in input().split()]
n = num[0]
m = num[1]
matrix = [[int(i) for i in input().split(' ')] for j in range(n)]
k = int(input())
for i in range(len(matrix)):
    m = 1
    count = 1
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0 and m <= k and j + m <= len(matrix[i])-1:
            if matrix[i][j+m] == 0:
                count += 1
                m += 1
    if count == k:
        print(i+1)

## Задача 6 - Дан прямоугольный массив размером n×m. Поверните его на 90 градусов по часовой стрелке, записав результат в новый массив размером m×n.

num = [int(i) for i in input().split()]
n = num[0]
m = num[1]

matrix = [[int(i) for i in input().split()] for i in range(n)]
matrix_final = [[0 for j in range(n)] for i in range(m)]
matrix.reverse()
for i in range(n):
    for j in range(m):
         matrix_final[j][i] = matrix[i][j]

for i in matrix_final:
    print(*i)
