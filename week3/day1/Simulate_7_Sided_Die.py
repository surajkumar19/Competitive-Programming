# Worst-case O(∞) time (we might keep re-rolling forever)
import random


def rand5():
    return random.randint(1, 5)


def rand7():
    # Implement rand7() using rand5()
    while True:
        value = 5 * (rand5() - 1) + rand5()
        if value <= 21:
            return value % 7 + 1


for x in range(10):
    print(rand7(), end=" ")
