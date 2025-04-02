def sumlist(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    print(sumlist(l))
    print(sum(l))
    print(sumlist(l) is sum(l))
