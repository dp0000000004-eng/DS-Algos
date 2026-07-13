class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        seen = 0
        ans = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                seen += 1
            elif nums[i] == 0:
                if seen >= ans:
                    ans = seen
                    seen = 0
                elif seen < ans:
                    seen = 0

            if i == (len(nums)-1) and seen > ans:
                ans = seen


        return ans  

nums = [1, 1, 1, 1, 1, 0, 1, 0, 1,1, 1, 1, 0, 1]


sol = Solution()
ans = sol.findMaxConsecutiveOnes(nums)
print(ans)