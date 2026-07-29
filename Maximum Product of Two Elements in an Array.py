class Solution:
    def maximumProductofTwoElementsinanArray(self, nums: list[int] ) -> int:

        l = float('-inf')
        sL = float('-inf')

        for num in nums:
            if num >= l:
                sL = l
                l = num
            elif num > sL:
                sL = num

        return l , sL



nums = [1,5,4,5]

sol = Solution()
ans = sol.maximumProductofTwoElementsinanArray(nums)
print(ans)