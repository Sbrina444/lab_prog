#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')



# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
lion = zoo.index('lion')+1
lark = zoo.index('lark')+1
print(zoo)
print('Лев сидит в',lion, 'клетке')
print('Жаворонок сидит в',lark, 'клетке')