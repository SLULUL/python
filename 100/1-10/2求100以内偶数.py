def fun():
    for i in range(0, 101, 2):
        print(i, end=" ")
fun()
print()
l = [x for x in range(0,101) if x%2==0]
print(l)