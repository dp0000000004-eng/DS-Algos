nums = [1]
nums.sort()

ans = 0
for i, num in enumerate(nums):
    try:
        if nums[0] != 0:
            ans = 0
            break
        elif num + 1 != nums[i+1]:
            print(num + 1)
            break
    except IndexError:
        ans = max(nums)+1 

print(ans)