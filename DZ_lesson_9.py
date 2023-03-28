## Задача 1 - Напишите класс Python для преобразования целого числа в римскую цифру
## Задача 2 - Напишите класс Python для преобразования римской цифры в целое число

###Сделал, так, что при вводе арабской цифры выведет римскую, а при вводе римской выведет арабскую!

class Rim_num:
    def __init__(self, num):
        self.__num = num

    def transformation(self):
        try:
            self.__num = int(self.__num)
            rim_1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
            rim_10 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            rim_100 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            rim_1000 = ["", "M", "MM", "MMM", "MMMM"]
            arab_1000 = rim_1000[self.__num // 1000]
            arab_100 = rim_100[self.__num // 100 % 10]
            arab_10 = rim_10[self.__num // 10 % 10]
            arab_1 = rim_1[self.__num % 10]
            print(arab_1000 + arab_100 + arab_10 + arab_1)
            #return arab_1000 + arab_100 + arab_10 + arab_1
        except Exception:
            self.__num = self.__num
            d_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            d_2 = {('I', 'V'): 3, ('I', 'X'): 8, ('X', 'L'): 30, ('X', 'C'): 80, ('C', 'D'): 300, ('C', 'M'): 800}
            num = 0
            prev_num = 0
            for number in self.__num:
                if prev_num and d_1[prev_num] < d_1[number]:
                    num += d_2[(prev_num, number)]
                else:
                    num += d_1[number]
                    prev_num = number
                # return num
            print(num)

rim_num = Rim_num(input())
rim_num.transformation()

