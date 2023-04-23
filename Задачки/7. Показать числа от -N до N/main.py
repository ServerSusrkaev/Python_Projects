number = int(input("Введите число: "))

index = number - (number * 2)

while index <= number:
    print(index, end=", ")
    index += 1