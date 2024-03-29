from random import randint

number = randint(1, 100)
# Назначаем переменную, в котором будет выбрано случайное число из интервала 
# от 1 до 100.
print('Угадайте число от 1 до 100')

# Назначаем цикл while, который позволит прервать цикл только после равенства 
# загаданного числа и введенного игроком.
while True:
    # Запрашиваем у игрока ввести число.
    guess = int(input('Введите целое число: '))

    # Далее начинаем через условные операторы сравнивать, что ввел игрок, с тем,
    # что загадал компьютер.
    if guess > number:
        print('Ваше число больше загаданного')

    elif guess < number:
        print('Ваше число меньше загаданного')

    elif guess == number:
        break  # Прерываем цикл как только установится равенство

print('Вы угадали, sir!')
