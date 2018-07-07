# O(n)
from random import randint


def random(min_value, max_value):
    return randint(min_value, max_value)


def shuffle(the_list):
    # Shuffle the input in place
    length = len(the_list)
    for i in range(0, length - 1):
        j = random(i, length - 1)
        the_list[i], the_list[j] = the_list[j], the_list[i]

    return the_list


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
