import csv
import json

path = 'C:/Users/AndreuKh/PycharmProjects/pythonProject/'
title = 'qwe.json'
file_name = path+title

users= {1:'Vadim',
        2: 'Irina',
        'name': 'Alex'}


users_2= {1:'Vadim',
        2: 'Irina',
        3: ['Alex', 'Olga', 'Victor']}

users_3= {1:'Vadim',
        2: 'Irina',
        3: users}

users_4= {1:'Vadim',
        2: 'Irina',
        3: {'name':'Jora',
            'age': 30,
            'height':178,
            'Family': {
                'wife':"natasha",
                'children':['Anna', 'Alex']
            }}}
item_1 = users_4[3]['Family']['children'][1]

# users_4[3]['age'] = 40
#
# users_4.pop(2)
# # users_4[2] = 'Ignat'
# users_4.update({2:'Igor'})
# xx = users_4.copy()
# xx['salaru']=1000
# print(users_4)
# aa = {1:{'age':30},
#       1:{'age':39}}
# print(aa[1])

# for i,k in users_4.items():
#     print(i,k)

name = ['Vadim', 'Misha', 'Alex']
age = [30, 20, 40]


# u_4 = {}
#
# for i in range(0, len(name):
#     u_4[name[i]] = age[i]
# users_4_4 = dict.fromkeys(name,age)
# print(u_4)

with open(file_name, 'w') as jf:
    json.dump(users_4, jf)

with open(file_name, 'r') as jf:
    data= jf.read()
    js_obj = json.loads(data)

print(js_obj)
