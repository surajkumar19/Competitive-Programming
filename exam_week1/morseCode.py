
d = dict(A='.-', B='-...', C='-.-.', D='-..', E='.', F='..-.', G='--.', H='....', I='..', J='.---', K='-.-', L='.-..',
         M='--', N='-.', O='---', P='.--.', Q='--.-', R='.-.', S='...', T='-', U='..-', V='...-', W='.--', X='-..-',
         Y='-.--', Z='--..')


def morsecode(sent):
    s = ""

    for z in sent:
        s += d[z]
    return s


def Solution(lis):

    l=[]

    for x in lis:
        z = morsecode(x.upper())
        if z not in l:
            l.append(z)
    # print(l)
    return len(l)


print(Solution(["gin", "zen", "gig", "msg"]))
print(Solution(["a", "z", "g", "m"]))
print(Solution(["bhi", "vsv", "sgh", "vbi"]))
print(Solution(["a", "b", "c", "d"]))
print(Solution(["hig", "sip", "pot"]))


