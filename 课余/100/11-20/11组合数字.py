from itertools import permutations

# 生成1-4所有四位不重复排列
for nums in permutations([1,2,3,4], 3):
    print(''.join(map(str, nums)))