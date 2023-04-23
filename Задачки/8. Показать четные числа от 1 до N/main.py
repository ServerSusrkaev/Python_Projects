number = int(input("Введите число: "))
index = 1

while index <= number:
    if index % 2 == 0:
        print(index, end = " ")
    index += 1