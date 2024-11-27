# Работа со словарями
my_dict = {'Вася': 1975,'Егор': 1999,'Маша': 2002}
print( my_dict)

# Существующее и несуществующее значение
existing_value = my_dict.get('Маша')
not_existing_value = my_dict.get('Аня', None)
print("Existing value:", existing_value)
print("Not existing value:", not_existing_value)

# Добавление пар
my_dict['Камила'] = 1981
my_dict['Артем'] = 1915

# Удаление пары
deleted_value = my_dict.pop('Егор')
print("Deleted value:", deleted_value)

# Вывод измененного словаря
print("Modified dictionary:", my_dict)

# Работа с множествами
my_set = {1, 'Яблоко', 42.314, 1, 2, 'Яблоко'}
print(my_set)

# Добавление элементов
my_set.add(13)
my_set.add((5, 6, 1.6))

# Удаление элемента
my_set.remove(1)

# Вывод измененного множества
print("Modified set:", my_set)