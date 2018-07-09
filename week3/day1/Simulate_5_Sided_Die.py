# Worst-case O(∞) time (we might keep re-rolling forever)
import random


def rand7():
    return random.randint(1, 7)


def rand5():
    # Implement rand5() using rand7()
    value = rand7()
    if value <= 5:
        return value
    else:
        return rand5()


for x in range(10):
    print(rand5(), end=" ")
