nums = [2, 2, 1, 3]

cand1 = cand2 = None
count1 = count2 = 0
ans = []

for num in nums:
    if num == cand1:
        count1 += 1
    elif num == cand2:
        count2 += 1
    elif count1 == 0:
        cand1, count1 = num, 1
    elif count2 == 0:
        cand2 , count2 = num, 1
    else:
        count1 -= 1
        count2 -= 1

print(count1)
print(count2)

for cand in [cand1, cand2]:
    if cand is not None and nums.count(cand) > len(nums) // 3:
        ans.append(cand)
    
print(ans)