# task 5
"""Выведите n-ое число Фибоначчи, используя только временные
переменные, циклические операторы и условные операторы. n - вводится"""
""" Числа Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711"""
number_of_fibonacci_number = int(input("Введите номер числа из ряда: "))
start = 0
next_number = 1
for number in range(1, number_of_fibonacci_number):
    start, next_number = next_number, start + next_number
print(start)