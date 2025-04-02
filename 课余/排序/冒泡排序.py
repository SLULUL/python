def bubble_sort(original_list: list[int]) -> list[int]:
    lst = original_list.copy()  # 复制使其不会改变原有数组
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:  # 如果本轮没有交换，提前终止
            break
    return lst


if __name__ == '__main__':
    print(bubble_sort([4, 11, 3, 71, 444, 1, 2190, 0]))
