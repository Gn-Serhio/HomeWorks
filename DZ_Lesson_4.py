# Задача 1 - Найти расстояние между двумя локальными максимуми (локальный максимум - число, которое больше предыдущего
list = [1, 2, 1, 3, 4, 2, 1, 1, 3, 1]
list_max = []
max = list[0]
p_max = list[0]
for i in range (len(list)):
    if list[i] > max:
        max = list[i]
        max_index = list.index(max)
list_max.append(max)
del list[max]
list.insert(max_index, 0)
for i in range (len(list)):
    if list[i] > p_max:
        p_max = list[i]
for i in range(len(list)):
    if list[i] == p_max:
        list_max.append(i)
loc_max = 0 #abs(list_max[0] - list_max[1])
for i in range(len(list_max)):
        loc = abs(list_max[0] - list_max[i])
        if loc > loc_max:
            loc_max = loc - 1
print(loc_max)

# Задача 2 - Выведите все четные элементы массива.
# В 1-ой строке вводится количество элементов, во 2-ой сами элементы массива.

list = []
size = int(input())
for i in range(size):
    list.append(int(input()))
for i in range(len(list)):
    if list[i] % 2 == 0:
        print(list[i], end=" ")

# Задача 3 - Найти количество положительных элементов в массиве.
# В 1-ой строке вводится количество элементов, во 2-ой сами элементы массива.

list = []
size = int(input())
count = 0
for i in range(size):
    list.append(int(input()))
for i in list:
    if i > 0:
        count += 1
print(count)

# Задача 4 - Дан массив чисел. Выведите все элементы массива, которые больше предыдущего элемента.
# В 1-ой строке вводится количество элементов, во 2-ой сами элементы массива.

list = []
size = int(input())
for i in range(size):
    list.append(int(input()))
num = list[0]
for i in list:
    if i > num:
        print(i, end=' ')
        num = i
    else:
        num = i

# Задача 5 - Дан массив целых чисел. Если в нем есть два соседних элемента одного знака,
# выведите эти числа, если соседних элементов одного знака нет - не выводить ничего.
# Если таких пар соседей несколько - выведите первую пару.
# В 1-ой строке вводится количество элементов, во 2-ой сами элементы массива (отличные от 0).

list = []
size = int(input())
for i in range(size):
    list.append(int(input()))
num = list[0]
for i in list[1:]:
    if i > 0 and num > 0 or i < 0 and num < 0:
        print(num, i)
        num = i
        break
    else:
        num = i