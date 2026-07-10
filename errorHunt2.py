nums = [0]
k = len(nums)-1

if nums[k] <= 9:
    nums[k] = nums[k] + 1
def recaorsion(nums):
    for i in range(len(nums)):
        if nums[i] == 10:

            nums[i] = nums[i] % 10
            if nums[i-1] != 0 and 10:
                nums[i-1] = nums[i-1]  + 1
            elif nums[i-1] == 0 and 10:
                nums.insert(0, 1)
for i in nums:
    if i == 10:
        for i in range(len(nums)):
            recaorsion(nums)

print(nums)