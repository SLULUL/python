lst1 = [1, 2]
lst2 = [2, 3]
for i in range(2, 22):
    lst1.append(lst1[i-1]+lst1[i-2])
    lst2.append(lst2[i-1]+lst2[i-2])
suml = 0
for i in range(20):
    suml += lst1[i]/lst2[i]
print(suml)
