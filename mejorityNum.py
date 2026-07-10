from math import ceil

nums = [3, 1, 3, 5, 3, 6, 3, 6, 3]
nums.sort()

k  =  ceil(len(nums) / 2)-1

for i in range(len(nums)):
    if nums[i] == nums[k]:
        print(nums[k])
        break