# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран

a = 1
b = 2
print("Переменные a и b -", a, b)
n1 = int(input("Введите первое число "))
n2 = int(input("Введите второе число "))
s1 = input("Введите первую строку ")
s2 = input("Введите вторую строку ")

print("Введеные значения -", n1, n2, s1, s2)


# Пользователь вводит время в секундах. Переведите время в часы, минуты
# и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_sec = int(input("Введите время в секундах: "))
hours = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
seconds = residue % 60

print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))


# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = lambda x, n: int(str(x) * n)

num = int(input("Введите число: "))
print(num + n(num, 2) + n(num, 3))


# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("Введите число: ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print("Наибольшая цифра в числе:", x)


# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))

if proceeds > costs:
    print('Фирма работает с прибылью')
    income = proceeds - costs
    print('Рентабельность фирмы {:%}'.format(income / proceeds))
    employees = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль на одного сотрудника составляет {income / employees}')
elif proceeds == costs:
    print('Фирма работает в ноль')
else:
    print('Фирма работает без окупаемости')


# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
distance = a
day_counter = 1

while distance < b:
    day_counter += 1
    distance *= 1.1
print(f"Вы достигнете требуемых показателей на %.d день" % day_counter)


