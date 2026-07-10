nums = [2,2,3,1]

seen = set()
ans = 0

for i in nums:
    seen.add(i)


sorted_list = sorted(seen)

if len(seen) > 2:
    ans = sorted_list[len(sorted_list) - 3]
elif len(seen) <= 2:
    ans = max(sorted_list)


print(ans)