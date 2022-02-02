

# dict_data = {
#     'name':'Andreu',
#     'age': 31,
#     'weight': 67,
#     'food': {'milk':['curd','milk', 'protein'],
#              'meat':['pelmeni', 'meat', 'soiska v teste']},
#     'salary':[250,320,700,1100,1200,1500,2000]
# }
# count=0
# key_list = []
#
# for i,k in dict_data.items():
#     if k == 'food':
#         key_list = k['milk']
#     key_list.append(k)
#     print(i,'==',k)
#
#
# print('==============================')
# print(key_list)


# def ff(n):
#     return n*2
# items_list = [ff(i) for i in range(0,10) if i % 2 ==0 and i %4 == 0]
# print(items_list)
# items_list_2 =[]
# for ii in range(0,10):
#     items_list_2.append(ii)
#
# print(items_list_2)

import time
count = 0

# nn = count < 10
#
# while nn:
#     # time.sleep(.500)
#     print('Hello', count)
#     count+=1
#     nn = count < 10
#     if count == 100:
#         break

while True:
    input_value = input('Input your value:')
    if type(int(input_value)) !=int:
        print('Enter int pleace')
        continue



    nn = int(input_value) *2
    print('You value*2 = ',nn)
    if nn > 100:
        break