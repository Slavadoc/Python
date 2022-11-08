# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.//
# # Пример:
# # 6782 -> 23
# # 0,56 -> 11

# n = input("Введите число : ")

# def sum(_n):
#     sum = 0
#     for i in range(len(_n)):
#         if _n[i] != ',':
#             sum += int(_n[i])
#     return sum

# print(sum(n))

# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # Пример:
# # - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

# def numbers(_n):
#     sum = 1
#     for i in range(1, _n+1):
#         sum *= i
#     return sum

# def fillList(_m):
#     l = []
#     for i in range(1, _m+1):
#         l.append(numbers(i))
#     return l

# def printList(_list):
#     for z in range(len(_list)):
#         print(_list[z], end=' ')

# n = int(input("Введите число : "))
# listNumbers = fillList(n)
# printList(listNumbers)

# Задайте список из n чисел последовательности $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def numbers(_n):
    sum = 1
    for i in range(1, _n+1):
        sum += i
    return sum


def fillDict(_m):
    d = dict()
    for i in range(1, _m+1):
        d[i] = numbers(i)
    return d


def printDict(_d):
    for z in range(len(_d)):
        print(_d[z], end=' ')


n = int(input("Введите число : "))
nDict = fillDict(n)
print(nDict)

# Задайте список из N элементов, заполненных числами из промежутка[-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.
