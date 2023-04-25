number = int(input("Введите 3-х значное чило: "))

count = len(str(number))

if count < 3 or count > 3:
    print ("Число не является 3-х значным")
else:
    result = number % 100
    result = result % 10
    print(result)