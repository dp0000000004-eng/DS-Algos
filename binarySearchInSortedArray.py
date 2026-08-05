class Solution:
    def binarySearch(self, nums:list[int], target:int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:

            mid = (l + r) // 2


            if nums[mid] > target:

                r = mid -1

            elif nums[mid] < target:

                l = mid + 1

            else:

                return mid

        return -1


nums = [5]
target = -5

sol = Solution()
ans = sol.binarySearch(nums, target)
print(ans)