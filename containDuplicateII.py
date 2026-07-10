class Solution:
    def containDuplicate(self, nums:list[int], k: int) -> bool:


        seen = {}

        for i , num in enumerate(nums):
            if num in seen and abs(i - seen[num]) <= k:
                return True
            seen[num] = i
        else:
            return False


        


nums = [1,0, 1, 1]
k = 1

sol = Solution()

ans = sol.containDuplicate(nums, k)

print(ans)