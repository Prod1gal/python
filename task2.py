"""2. Для списка реализовать обмен значений 
соседних элементов, т.е. Значениями обмениваются 
элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний 
сохранить на своем месте. Для заполнения списка 
элементов необходимо использовать функцию input()"""

elements_count = int(input('Введите количество элементов'))
my_list = []
i = 0
e = 0
while i < elements_count:
    my_list.append(input('Введите следующее значение'))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[e], my_list[e + 1] = my_list [e + 1], my_list[e]
        e += 2
print(my_list) 
