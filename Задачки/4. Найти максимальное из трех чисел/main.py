# Найти максимальное из трех чисел

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

max = a

if max < b: max = b
if max < c: max = c


print("Максимальным числом является число: " + str(max))