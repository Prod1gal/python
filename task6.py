"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя."""


products = int(input("Введите количество товарных позиций: "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= products:
    my_dict = dict({'Название': input('Введите название товара: '), 'Цена': input('Добавьте цену товара: '), 'Количество': input('Введите количество товара: '), 'eд.': input('Добавьте единицу измерения для товара: ')})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict({'Название': my_dict.get('Название'), 'Цена': my_dict.get('Цена'), 'Количество': my_dict.get('Количество'), 'ед.': my_dict.get('ед.')})

print(my_list)