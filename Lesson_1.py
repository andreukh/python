import time
# enot_1 = 0
# # тип переменной
# print(type(enot_1))
# enot_1_1 = type(enot_1)
# print(enot_1_1)
#
# kotik_1 = 'Murzik'
# #c= enot_1*kotik_1

i_1 = 0
i_2 =10
I_2 = 3
i_3 =7
i_4=22
i_5=159
sqr = 49
tt=50
# print(i_3)
#
# s_1 = i_2+i_4
# m_1 = i_2 - i_3
# print('Summ_1=',s_1)
# print('m_1=',m_1)
#
# u_1= i_3 * i_2
# print('u_1=',u_1)
#
# d_1 = i_5 / I_2
# print('d_1=',d_1)
# d_2 = i_5 / i_4
# print('d_2=',d_2)

# степень
# sq = i_3**I_2
# print('sq=',sq)

# деление с остатком, остаток не указан
#do_1 = i_4//i_3
#print('d_1=',do_1, type(do_1))
#деление с остатком, вывод остатка
#dos_1 = i_4%i_3
#print('dos_1=',dos_1,type(dos_1))
#d_1 = i_4/i_3
#print('d_1=',d_1,type(d_1))

# dd = (i_3+i_2)*i_2
# print('dd=',dd)
# импорт библиотеки math
import math
# через math. - выбирается функция из библиотеки math
# mm=math.sqrt(sqr)
# print(mm)
# явное приведение ex: int(mm)
# mm=int(math.sqrt(sqr))
# print(mm, type(mm))
# aa=int(math.sqrt(tt))
# print(aa, type(aa))
# aa=math.sqrt(tt)
# print(aa, type(aa))

# vv = 7.9
# xx = 7
# qwe= 1.1231231241212
# print(int(vv))
# print(vv%-int(vv))
# print(vv-int(vv))
# # округление после запятой -количество знаков
# print(round(qwe, 5))

# изменение переменной +-/*
# i_2 +=2 # = i_2 = i_2 + 2
# print(i_2)
# возвращает ближайшее целое число, меньшее, чем указанное
#pp = math.floor(3.14)
#print(pp)
# округление всегда в большую сторону
#pp = math.ceil(3.14)
#print(pp)
# возведение в степень
#pp = math.pow(2, 2)
#print(pp)

#ветвления
# if True:
#     print('Hello i_2')
# if False: #не работает
#     print('Hello i_2')
#
# bb= True
# ff= False
# sss='123d'
# # если не равно
# if sss != '123d' :
#     print('Hello i_2')

# оператор сравнения возвращает булевый тип данных
# qq = i_3< 10
# print(qq)
# проверяет равна ли переменнаячислу, если равно true если нет то false
# qq = i_3 <= 10 # <= >= !=(не равно)
# print(qq)
qq =99
print(qq)
if qq == 77:
    print('Hello world')
elif qq==99:
    print('Hello 99')
else:
    print('Python')