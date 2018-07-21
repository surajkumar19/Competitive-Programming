def check(k):
    lis =[x for x in range(k+1)]
    l =[]
    for x in lis:
        z = "{0:b}".format(x)
        p = z.count('1')
        l.append(p)

    return l

print(check(15))
print(check(16))
print(check(1))
print(check(25))
print(check(5))
print(check(6))