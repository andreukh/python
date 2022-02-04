# def getNumber01():  # Первый вариант
#     while type:
#         getNumber = input('Введите число: ')                 # Ввод числа
#         try:                                    # Проверка что getTempNumber преобразуется в число без ошибки
#             getTempNumber = int(getNumber)
#         except ValueError:                      # Проверка на ошибку неверного формата (введены буквы)
#             print('"' + getNumber + '"' + ' - не является числом')
#         else:                                   # Если getTempNumber преобразован в число без ошибки, выход из цикла while
#             break
#     return abs(getNumber)                   # возвращает модуль getTempNumber (для искл. отрицат. чисел)
#
# print(getNumber01())

a = ['USD','EUR','CHF','GBP','CNY']
coef_usd = [1, 0.87, 0.92, 0.74, 6,36]
coef_eur = [1.15, 1, 1.06, 0.84, 7.29]
coef_chf = [1.08, 0.95, 1, 0.8, 6.9]
coef_gbr = [1.36, 1.19, 1.25, 1, 8.64]
coef_cny = [0.16, 0.14, 0.14, 0.12, 1]

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
          inp_2=int(inp_2)
     if inp_1 == 'USD':
          b= [float(i) for i in coef_usd]
          a1=[i*inp_2 for i in b]
          s=dict(zip(a[1:],a1[1:]))
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


# b = {a[:2]: 0.87, a[:3]: 0.92, a[:4]: 0.74, a[:5]: 6.36}

# print('\n'.join(b))
# b = [float(i) for i in coef_eur]
          # for i in coef_eur:
          #      b.append(float(i))



# print(a[1:], sep = '\n')

# print(a[:1])

