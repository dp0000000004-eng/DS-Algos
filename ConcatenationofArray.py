class Solution:
    def ConcatenationofArray(self, nums: list[int] ) -> list[int]:

        for num in nums:
            nums.append(num)

        # return nums
        

nums = [1, 2, 3, 4]

sol = Solution()
ans = sol.ConcatenationofArray(nums)
print(ans)