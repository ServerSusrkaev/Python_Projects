age = int(input('Введите ваш возраст: '))

if age < 18:
    print('Доступ запрещен!')
elif age == 18:
    print('Вам ровно 18 лет')
else:
    print('Доступ разрешен!')