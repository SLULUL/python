# def fun(l1):
#     return [x for x in l1]


# l1 = ['a', 'b', 'c', 'd']
# l2 = fun(l1)
# print(l2)
# l1[1] = 'v'
# print(l2)
import copy
l1 = ['a', 'b', 'c', 'd']
l2 = copy.copy(l1)
print(l2)
l1[0] = '2'
print(l2)
