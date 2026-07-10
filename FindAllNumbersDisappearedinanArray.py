class Solution:
    def findAllNumbersDisappearedinanArray(self, nums:list[int]) -> list[int]:
        if len(nums) > 2:
            nums = list(set(sorted(nums)))
        print(nums)

        ans = []
        try:
            for i in range(len(nums)-1):
                if nums[0] != 1:
                    ans.append(1)
                elif (nums[i] + 1) != nums[i+1]:
                    nums[i+1] = nums[i] + 1
                    ans.append(nums[i] + 1)
                    continue
        except IndexError:
            pass
        


        return ans
    
nums = [4,3,2,7,8,2,3,1]

sol = Solution()
ans = sol.findAllNumbersDisappearedinanArray(nums)
print(ans)