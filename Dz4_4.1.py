#Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

n = int(input("Введите количество элементов: "))
m = int(input("Введите количество элементов: "))

my_list = []
my_list_1 = []

for i in range(n):
    my_list.append(random.randint(0, 100))

for i in range(m):
    my_list_1.append(random.randint(0, 100))

my_list = list(set(my_list))
my_list.sort()
my_list_1 = list(set(my_list_1))
my_list_1.sort()

print(my_list)
print(my_list_1)