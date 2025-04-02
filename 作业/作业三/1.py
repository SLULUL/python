def millennium_bug(lst: list) -> list:
    lst1 = lst.copy()
    for i, j in enumerate(lst1):
        if 0 <= j <= 25:
            lst1[i] += 2000
        else:
            lst1[i] += 1900
    return lst1


if __name__ == '__main__':
    s = input("请输入序列，以“,”分隔")
    lst = [int(x) for x in s.split(",")]
    print(f'输出序列{millennium_bug(lst)}')
