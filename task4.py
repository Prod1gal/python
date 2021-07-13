"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень."""

digit = (int, float, complex)

def my_func(base: digit, exp: digit, mod: digit = None) -> digit:
    if not isinstance(base, digit) or not isinstance(exp, digit):
        raise TypeError(f"Неподдерживаемый тип операнда: "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}'")
    if mod and not isinstance(mod, digit):
        raise TypeError(f"Неподдерживаемый тип операнда: "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")
    result = base ** exp

    if mod is None:
        return result
    else:
        return result % mod

def my_func_1(base: digit, exp: digit, mod: digit = None) -> digit:
    if not isinstance(base, digit) or not isinstance(exp, digit):
        raise TypeError(f"Неподдерживаемый тип операнда: "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}'")
    if mod and not isinstance(mod, digit):
        raise TypeError(f"Неподдерживаемый тип операнда: "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")
    result = 1

    while exp:
        result *= base
        exp -= 1
    if mod is None:
        return result
    else:
        return result % mod

if __name__ == '__main__':
    print(my_func(10, 100))
    print(my_func_1(10, 20, 30))
