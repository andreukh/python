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
        if type(number_1) == int and number_1 !=0 :
            number_1 = int(number_1)
            print('Ты ввёл ', number_1, 'rub')
            print('Конвертированная сумма в USD =', int(number_1 / 76.26))
            print('Конвертированная сумма в EUR =', int(number_1 / 86.04))
            print('Конвертированная сумма в CHF =', int(number_1 / 82.80))
            print('Конвертированная сумма в GBR =', int(number_1 / 103.15))
            print('Конвертированная сумма в CNY =', int(number_1 / 12.02))
            break
        elif number_1 <0:
                    print('Please, enter a positive number ')
                    number_1 = input()
                    continue
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