number = int(input("Введите трехзначное число: "))
result = str(number // 100)
result += str(number % 10)

print(result)