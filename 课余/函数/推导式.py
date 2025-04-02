l = [x ** 2 for x in range(1, 11) if x**2 % 2 != 0]
print(l)
t = tuple(x ** 2 for x in range(1, 11))
print(t)
d = {x: x**2 for x in range(1, 11)}
print(d[10])
L = ['ReD', 'GrEeN', 'BlUe']
D = {c.lower(): c.upper() for c in L}
print(D)
