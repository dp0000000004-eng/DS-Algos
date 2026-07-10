from math import floor

nums = [0, 2, 4, 2]

chose = 0


def makeItZero():
    k = 0
    for i, num in enumerate(nums):
        if num >= 2:
            nums[i] = num - 2
        k = k+1

    return k

