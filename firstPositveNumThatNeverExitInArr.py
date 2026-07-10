class Solution:
    def firstPositiveNum(self, nums:list[int] ) -> int:
        nums.sort()
        k = 1
        ans = 0
        for i in range(len(nums)):
            try:
                if nums[k] - nums[i] == 1:
                    k += 1
                    i += 1
                else:
                    ans = nums[i] + 1
            except IndexError:
                ans = nums[i] + 1
        
        return ans


nums = [2, 1 ,0, 5]
sol = Solution()
ans = sol.firstPositiveNum(nums)
print(ans)