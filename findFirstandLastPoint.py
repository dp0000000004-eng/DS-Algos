class Solution:
    def findFirstAndLast(self, nums:list[int], target:int) -> list[int]:
        
        seen = {}
        ans = []

        for i, num in enumerate(nums):
            if num == target:
                ans.append(i)

        if target not in nums:
            for i in range(2):
                ans.append(-1)

        return [ans[0], ans[len(ans)-1]]
 
nums = []

target = 0

sol = Solution()
ans = sol.findFirstAndLast(nums, target)
print(ans)