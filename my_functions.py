def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    return '*' * 10

result = simple_separator()
print("Результат функции:", result)


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    separator = '*' * count
    print(separator)
    return separator

def separator(symbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param symbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    separator = symbol * count
    print(separator)
    return separator


class Print:
    pass


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********
    Hello World!
    ##########
    :return: None
    """
    print(simple_separator())
    print()
    print("Hello World!")
    print()
    print("#" * 10)

hello_world()


def hello_who(who='World'):
    name = input("Введите ваше имя: ")
    print(simple_separator())
    print("Hello {}!".format(name))
    print(long_separator(10))
hello_who()


def pow_many(power, *args):
    return sum(args) ** power
print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} --> {v}')
"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)

def my_filter(iterable, function):
    return list(filter(function, iterable))
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])