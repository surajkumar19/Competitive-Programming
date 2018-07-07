def ckeck_all_rooms(rooms):
    rooms_list = [False] * (len(rooms))
    temp_list = []
    rooms_list[0] = True

    try:

        for x in rooms[0]:
            temp_list.append(x)
            rooms_list[x] = True

        while len(temp_list) != 0:
            for x in rooms[temp_list[0]]:
                if x not in temp_list and rooms_list[x] is False:
                    temp_list.append(x)
                rooms_list[x] = True
            temp_list.remove(temp_list[0])

    except:
        print("wrong")
        return

    for x in rooms_list:
        if x is False:
            print(False)
            break
    else:
        print(True)


ckeck_all_rooms([[1], [0, 2], [3]])
ckeck_all_rooms([[1, 3], [3, 0, 1], [2], [0]])
ckeck_all_rooms([[1, 2, 3], [0], [0], [0]])
ckeck_all_rooms([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
ckeck_all_rooms([[1], [2, 3], [1, 2], [4], [1], [5]])
ckeck_all_rooms([[1], [2], [3], [4], [2]])
ckeck_all_rooms([[1], [1, 3], [2], [2, 4, 6], [], [1, 2, 3], [1]])
