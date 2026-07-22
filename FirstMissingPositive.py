nums = []
size = len(nums)
big = max(nums)
big_num = max(size, big)

for i in range(big_num):
    if i+1 not in nums:
        print(i+1)
        break
else:
    print(1)