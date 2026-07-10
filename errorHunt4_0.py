nums = [1, 2, 3 , 4, 1]

seen = {}


for i, num in enumerate(nums):
    if num in seen:
        print(i, seen[num])
    seen[num] = i