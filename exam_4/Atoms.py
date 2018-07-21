def atoms(s):
    capital  ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small ="abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"

    d = {}
    ss =""
    for z in s:
        if z in capital or z in small:
            ss+=z
    bool = False
    for i in range(len(ss)-1):
        if ss[i+1] in small:
            d[ss[i:i+2]] = 1
        elif ss[i] in capital:
            d[ss[i:i+1]] = 1
    if ss[len(ss)-1] in capital:
        d[ss[len(ss)-1]] = 1

    if "(" not in s and ")" not in s:
        p = d.keys()
        l=[]
        for x in p:
            l= s.split(x)

atoms("K4(ON(SO3)2)2")
atoms("Mg(OH)2")
