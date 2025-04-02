for i in range(100, 1000):
    if (i%10)**3 + (i//10%10)**3 + (i//100) == i :
        print(i)