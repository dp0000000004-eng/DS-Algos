from collections import Counter

nums = [0,1,2,2,4,4,1]

even_nums = []

for i in nums:
    if i % 2 == 0:
        even_nums.append(i)

track = 0
ans = 0

even_nums.sort()
counts = Counter(even_nums)
print(counts[0])

for i in even_nums:
    if counts[i] > track:
        track = counts[i]
        ans = i

print(even_nums)

if even_nums == []:
    print(-1)

print(ans)