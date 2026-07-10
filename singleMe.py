nums = [1, 0 ,1]
nums.sort()
i = 0
k = 1
ans = 0

for _ in range(len(nums)):
    try:
        if nums[i] != nums[k]:
            ans = nums[i]
            break
    except IndexError:
        ans = nums[len(nums)-1]
    else:
        i += 2
        k += 2
        

print(ans)