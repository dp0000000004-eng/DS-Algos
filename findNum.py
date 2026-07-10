nums = [1,3,5,6]
r = 5

k = 0
store = set()

for i in nums:
    store.add(i)

for i in range(len(nums)):
    if nums[i] == r:
        k = i
        break
    elif nums[i] > r:
        k = i
        break
else:
    k = len(nums)

print(k)