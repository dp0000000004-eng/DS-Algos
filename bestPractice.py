
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        seen = {}
        ans = -1

        for i , num in enumerate(nums):
            current_num = num
            if current_num in seen:
                ans = seen[current_num]
            seen[current_num] = i
        
        return ans
nums = [1,2, 3, 4]
target = 4

sol = Solution()
ans = sol.search(nums, target)
print(ans)