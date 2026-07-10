class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int, add=0) -> bool:
        
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
                seen[num] = num
            return False

nums = [1, 0,1 , 1]
k = 1

sol = Solution()
ans = sol.containsNearbyDuplicate(nums, k)
print(ans)