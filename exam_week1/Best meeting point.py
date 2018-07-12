def best_meeting_point(l):
    a = len(l)
    b = len(l[0])
    Matrix = [[0 for x in range(b)] for y in range(a)]
    min = 10000
    for i in range(a):
        for j in range(b):
            count = 0
            for m in range(a):
                for n in range(b):
                    if l[m][n] == 1:
                        count += abs(m-i) + abs(n-j)
            Matrix[i][j]=count
            min = count if min>count  else min
    print(min)

test1 = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
test2 = [[1, 0, 1, 0, 1], [0, 1, 0, 0, 0],  [0, 1, 1, 0, 0]]
test3 = [[1, 1], [1, 1]]
test4 = [[0, 0], [0, 0]]
test5 = [[1, 0], [0, 0]]

best_meeting_point(test1)
best_meeting_point(test2)
best_meeting_point(test3)
best_meeting_point(test4)
best_meeting_point(test5)

