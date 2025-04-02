l = ['a', 'b', 'c', 'd']
for i, j in enumerate(l):
    print(i, j)
l2 = [["空" for _ in range(10)] for _ in range(10)]
print('\n'.join(' '.join(row) for row in l2))
