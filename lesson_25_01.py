import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--num_1', type=int, required=True)
parser.add_argument('--num_2', type=int, required=True)
parser.add_argument('--action', type=str)
args = parser.parse_args()

item_1 = args.num_1
item_2 = args.num_2
act = args.action

if act == 'sum':
    result = item_1 + item_2
    print('Result = ',result, type(result))
elif act == 'multi':
    result = item_1 * item_2
    print('Result = ', result, type(result))
elif act == 'div':
    result = item_1 / item_2
    print('Result = ', result, type(result))
elif act == 'sub':
    result = item_1 - item_2
    print('Result = ', result, type(result))

# args_dict = args.__dict__
#
# for k,v in args.__dict__.items():
#     print(k,v)

