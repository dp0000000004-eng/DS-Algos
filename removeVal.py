class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        size = len(nums)
        
        for num in nums[k:]:
            if num == val:
                nums.remove(num)
                k += 1

        return size - k

nums = [2,2, 2, 1, 1, 8, 1]
val = 1

sol = Solution()
ans = sol.removeElement(nums, val)
print(ans)