class Solution:
    def search(self, nums:list[int], target:int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left + right) // 2 

        if target == nums[middle]:
            return middle
        elif nums[left] <= nums[middle]:


        return middle


nums = [1,2 , 3, 4, 5, 6]
target = 2

sol = Solution()
ans = sol.search(nums, target)
print(ans)