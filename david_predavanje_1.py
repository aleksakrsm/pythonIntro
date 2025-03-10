import functools
a = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 0)
a = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(a)

a = [1,2,3,4,5]
b = [11,22,33,44,55]

c = zip(a,b)
print(c)
print(*c)


c = {2:12, 3: 78, 4:8}
c1 = {v:k for k,v in c.items()}
print(c1)