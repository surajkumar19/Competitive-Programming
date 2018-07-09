# Worst-case O(∞) time (we might keep re-rolling forever)
import random


def rand5():
    return random.randint(1, 5)


def rand7():
    # Implement rand7() using rand5()
    ans = rand5() + rand5()
    if ans <= 7:
        return ans
    else:
        return rand7()


for x in range(10):
    print(rand7(), end=" ")
