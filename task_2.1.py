# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

l = [1, '2', 'три', True, False, 1.23, [100, '200', 'триста'], None]

print('Список l: ', l)
print('Длина списка l:', len(l))

print('\n Перебор списка с использованием range:')
for i in range(len(l)):
    print(f'{i}-ый элемент списка имеет тип {type(l[i])} и равен {l[i]}')

print('\n Перебор списка с использованием enumerate:')
for i, el in enumerate(l):
    print(f'{i}-ый элемент списка имеет тип {type(el)} и равен {el}')

print('\n Проверка типа элементов списка при помощи isinstance()')
for i in range(len(l)):
    if isinstance(l[i], int):
        print(f'Тип {i}-ого элемента списка является целочисленным')
    elif isinstance(l[i], str):
        print(f'Тип {i}-ого элемента списка является строковым')
    elif isinstance(l[i], float):
        print(f'Тип {i}-ого элемента списка является числом с плавающей запятой')
    elif isinstance(l[i], list):
        print(f'Тип {i}-ого элемента списка является списком')
    else:
        print(f'Тип {i}-ого элемента списка является {type(l[i])}')

print('\n Перевернутый список: ', l[::-1])