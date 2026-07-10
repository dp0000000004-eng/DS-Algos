nums = [0, 1, 2, 0, 3]

for i in nums:
    if i == 0:
        nums.remove(i)
        nums.append(i)

print(nums)