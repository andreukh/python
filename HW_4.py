# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# number_1 = input('Enter your currency euro value:')
# while True:
#     if number_1.isdigit():
#         number_1 = int(number_1)
#         print('Ты ввёл ', number_1, 'euro')
#         a = int(number_1) / 0.8856
#         print('конвертированная сумма в USD = ', int(a))
#         break
#     else:
#         print('"' + number_1 + '"', 'Not is number. Please, enter number')
#         number_1 = input()
#         continue

# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.

# number_1 = input('Enter your currency rub value:')
# while True:
#     if number_1.isdigit():
#         number_1 = int(number_1)
#         print('Ты ввёл ', number_1, 'rub')
#         print('Конвертированная сумма в USD =', int(number_1 / 76.26))
#         print('Конвертированная сумма в EUR =', int(number_1 / 86.04))
#         print('Конвертированная сумма в CHF =', int(number_1 / 82.80))
#         print('Конвертированная сумма в GBR =', int(number_1 / 103.15))
#         print('Конвертированная сумма в CNY =', int(number_1 / 12.02))
#         break
#     else:
#         print('"' + number_1 + '"', 'Not is number. Please, enter number')
#         number_1 = input()
#         continue

# Задача 3
number_1 = input('Enter your currency rub value:')
while True:
    if number_1.isdigit():
        number_1 = int(number_1)
        if type(number_1) == str:
            print('"' + number_1 + '"', 'Is not a number. Please, enter a number')
            number_1 = input()
            continue
        elif number_1 == "":
            print('You have entered an empty field. Enter a number')
            number_1 = input()
            continue
        elif number_1 <0:
                    print('Please, enter a positive number ')
                    number_1 = input()
                    continue
        if type(number_1) == int and number_1 !=0 :
            number_1 = int(number_1)
            print('Ты ввёл ', number_1, 'rub')
            print('Конвертированная сумма в USD =', int(number_1 / 76.26))
            print('Конвертированная сумма в EUR =', int(number_1 / 86.04))
            print('Конвертированная сумма в CHF =', int(number_1 / 82.80))
            print('Конвертированная сумма в GBR =', int(number_1 / 103.15))
            print('Конвертированная сумма в CNY =', int(number_1 / 12.02))
            break
    # Задача 4
    убрать из списка валюту которую конвертируем, через цикл(?) и.или копию списка
    a = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']
    coef_usd = [1, 0.87, 0.92, 0.74, 6, 36]
    coef_eur = [1.15, 1, 1.06, 0.84, 7.29]
    coef_chf = [1.08, 0.95, 1, 0.8, 6.9]
    coef_gbr = [1.36, 1.19, 1.25, 1, 8.64]
    coef_cny = [0.16, 0.14, 0.14, 0.12, 1]
    dict(zip(a, coef_eur))
    while True:
        print('Выберите валюту из ', a)
        inp_1 = input()
        print('Введите сумму')
        inp_2 = input()
        print('Вы ввели сумму ', inp_2, 'Валюта - ', inp_1)

        if type(inp_2) == str:
            print('"' + inp_2 + '"', 'Is not a number. Please, enter a number')
            inp_2 = input()

        elif inp_2 == "":
            print('You have entered an empty field. Enter a number')
            inp_2 = input()

        elif inp_2 < 0:
            print('Please, enter a positive number ')
            inp_2 = input()
        if inp_2.isdigit():
            inp_2 = int(inp_2)
        if inp_1 == 'USD':
            b = [float(i) for i in coef_usd]
            a1 = [i * inp_2 for i in b]
            s = dict(zip(a[1:], a1[1:]))
            print(s)
        elif inp_1 == 'EUR':
            b = [float(i) for i in coef_eur]
            a1 = [i * inp_2 for i in b]
            s = dict(zip(a[::], a1[::]))
            print(s)
        elif inp_1 == 'CHF':
            b = [float(i) for i in coef_chf]
            a1 = [i * inp_2 for i in b]
            s = dict(zip(a[::], a1[::]))
            print(s)
        elif inp_1 == 'GBR':
            b = [float(i) for i in coef_gbr]
            a1 = [i * inp_2 for i in b]
            s = dict(zip(a[::], a1[::]))
            print(s)
        elif inp_1 == 'CNY':
            b = [float(i) for i in coef_cny]
            a1 = [i * inp_2 for i in b]
            s = dict(zip(a[::], a1[::]))
            print(s)


    # elif type(number_1) == str:
    #     print('"' + number_1 + '"', 'Is not a number. Please, enter a number')1
    #     number_1 = input()
    #     continue
    # elif number_1 == "":
    #     print('You have entered an empty field. Enter a number')
    #     number_1 = input()
    #     continue
    # else:
    #     print('"' + number_1 + '"', 'Not is number. Please, enter number')
    #     number_1 = input()
    #     continue

    #Задача 4

