class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        seen = {}
        output = []

        for i , num in enumerate(nums):
            k = target - num
            if k in  seen:
                output.append(seen[k])
                output.append(i)
            else:
                seen[num] = i
                
        return output

nums = [3,3]
target = 6

sol = Solution()
ans = sol.twoSum(nums, target)
print(ans)