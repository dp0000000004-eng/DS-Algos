class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        k = 0
        ans = []
        
        for i in nums1[k:]:
            for o in range(len(nums2)):
                if nums2[o] == i:
                    ans.append(i)
                    k = nums1.index(i)
                    break
            if len(nums2) == 1:
                break


        return ans

nums1 = [3, 2, 1]
nums2 = [1]

sol = Solution()
ans = sol.intersect(nums1, nums2)
print(ans)