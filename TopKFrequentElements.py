from collections import Counter

nums = [1, 7,7]

count = Counter(nums)

print(count)

print(count.most_common()[0][0], count.most_common()[1][0])