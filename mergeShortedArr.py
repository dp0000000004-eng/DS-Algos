nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 3, 4]

for _ in range(len(nums2)):
    nums1.pop()

for num in nums2:
    nums1.append(num)

k = 1

nums1.sort()

print(nums1)