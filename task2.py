"""2. Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def my_func(name, surname, birth_year, city, email, phone):
    return ' '.join([name, surname, birth_year, city, email, phone])
print(my_func(name='Иван', surname='Иванов', birth_year='1920', city='Moscow', email='ivanov@gmail.com',
                  phone='8-900-000-00-00'))