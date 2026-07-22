nums =  [9,1,4,7,3,-1,0,5,8,-1,6]

nums.sort()
print(nums)

k = 0


for i in range(len(nums)):
    try:
        if nums[i] + 1 == nums[i+1]:
            k += 1
        elif nums[i] == nums[i+1]:
            continue
    except IndexError:
        k += 1
        break

print(k)