# 猴子排序：即给定一个列表，如果没排好序，那么不断把列表打乱直至排好序
import random


def Is_Sorted(l1: list[int]) -> bool:
    for i in range(len(l1)-1):
        if l1[i] > l1[i+1]:
            return False
    return True


def Bogo_Sort(l1: list[int]) -> list[int]:
    lst = l1.copy()
    count = 0

    while not Is_Sorted(lst):
        random.shuffle(lst)
        count += 1

    print(f"排序次数：{count}")
    return lst


if __name__ == '__main__':
    print(Bogo_Sort([1, 2, 3, 9, 5, 6, 7, 8]))
