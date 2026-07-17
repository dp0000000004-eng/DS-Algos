class Solution:
    def replaceElementFromRight(self, nums:list[int]) -> list[int]:

        for i in range(len(nums)):
            try:
                nums[i] = max(nums[i+1:])
            except ValueError:
                nums[len(nums)-1] = -1

        return nums

nums = [3,3]

sol = Solution()
ans = sol.replaceElementFromRight(nums)
print(ans)