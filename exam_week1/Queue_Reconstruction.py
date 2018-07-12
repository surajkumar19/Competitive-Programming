def Queue_Reconstruction(Q):
    l=[]

    for z in Q:
        if z[1] == 0:
            l.append(z)
            Q.remove(z)
    l.sort()
    Q.sort()
    # print(l)
    Q=Q[::-1]
    # print(Q)



    for z in Q:
        val = check(l,z)
        if val == len(l):
            l.append(z)
        else:
            l.insert(val, z)
        # print(l)

    print(l)
    return None


def check(l, value):

    count =0
    for i in range(len(l)):
        kk = l[i][0]
        if l[i][0] >= value[0]:
            count+=1
            if count == value[1]:
                return i+1

# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Queue_Reconstruction([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
Queue_Reconstruction([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])
Queue_Reconstruction([[6,0], [5,1], [4,2], [3,3], [2,4], [1,5]])