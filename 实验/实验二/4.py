import random


def key():
    lst = list(range(ord('A'), ord('A')+26)) + \
        list(range(ord('1'), ord('1')+9))
    return ''.join(chr(c) for c in random.choices(lst, k=5))


if __name__ == '__main__':
    Sequence = '-'.join(key() for _ in range(5))
    print(Sequence)
