"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове."""

my_str = input('Введите несколько слов через пробел: ')
my_word = []
num = 1
for elements in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [elements]}")
        num += 1
    else:
        print(f" {num} {my_word [elements] [0:10]}")
        num += 1
