class Solution:
    def twoSum(self, nums: list[int], target:int) -> list[int]:

        seen = {}
        ans = []

        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                ans.append(i)
                ans.append(seen[comp])
            seen[num] = i

        ans.sort()

        for i in range(len(ans)):
            ans[i] = ans[i] + 1

        return ans

nums = [1, 2, 3, 4]
k = 3

sol = Solution()
ans = sol.twoSum(nums, k)
print(ans)