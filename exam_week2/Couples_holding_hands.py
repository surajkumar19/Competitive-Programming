def patner(i):
    if i % 2 == 0:
        return i + 1
    else:
        return i - 1


def swaps(list_people):
    count = 0
    for x in range(0, len(list_people), 2):
        other = patner(list_people[x])
        if list_people[x + 1] != other:
            exchange(other, x + 1, list_people)
            count += 1

    print(str(list_people) + "  " + str(count))


def exchange(i, j, list_people):
    a = list_people.index(i)

    list_people[a], list_people[j] = list_people[j], list_people[a]


swaps([1, 3, 4, 0, 2, 5])
swaps([3, 2, 0, 1])
swaps([0, 1])
# swaps([55,37,19,46,66,32,7,81,33,76,0,28,92,26,99,6,56,29,17,52,90,79,91,83,12,40,82,84,2,21,11,68,98,34,73,10,57,58,64,36])
# swaps([50,23,76,19,16,70,35,68,41,49,99,71,59,95,89,33,22,7,54,83,24,0,18,64,11,14,77,26,42,21,82,1,97,52,65,79,37,62,60,91,98,4,88,36,51,20,85,90,29,84,93,13,80,6,55,48,2,40,46,81,30,3,94,38,27,31,53,86,32,96,8,58,73,5])
