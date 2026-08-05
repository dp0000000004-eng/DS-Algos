class Solution:
    def findMissingNumbers(self, nums:list[int]) -> list[int]:
        nums.sort()

        ans = []

        for i in range(min(nums), max(nums)):
            if i not in nums:
                ans.append(i)
                continue

        return ans


nums = [1, 2, 4, 6]

sol = Solution()
ans = sol.findMissingNumbers(nums)
print(ans)