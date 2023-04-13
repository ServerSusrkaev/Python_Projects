#name = input('Кто создатель Python?: ')

#while name != 'Гвидо':
    #print('Ответ не верный. Повторите попытку: ')
    #name = input('Кто создатель Python?: ')
#print('Вы ответили верно!')

number = 0
n = int(input('Введите значение: '))
#while number <= n:
#    print(number)
#    number += 1

while number <= n:
    if number % 2 != 0:
        print(number)
    number += 1