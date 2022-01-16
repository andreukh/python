a = 'enot'
b = 'polosatiy'

c = a + b

d= 3
# error:
# result = a + d
# если так, то d-строка:
# d = str(3)
# result = a + d
d=3

# если так, то d-строка только в этом выражении:
result = a + str(d)
print(a, b)
print(a + ' ' + b)
print(result)
print('type d', type(d))
# умножение строки на число
print(a*d)
# умножение элемента строки [] на число
print(a[1]*d)
# странная срань:
print(a+a[1]*3+a[:2])
-
