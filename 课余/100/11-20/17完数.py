def fun ():
    for i in range(1,10000):
        sum = 0
        for j in range(1,i-1):
            if(i%j == 0):
                sum += j
        if sum == i :
            print(i)
fun()