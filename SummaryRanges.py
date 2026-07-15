class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        a = 0
        b = 0

        ans = []
        
        for i in range(len(nums)):
            try:
                if nums[i] + 1 == nums[i+1]:
                    if nums[i] == b:
                        b = nums[i+1]
                        ans.append(f"{a}->{b}")
                    else:
                        a = nums[i]
                        b = nums[i+1]
                        ans.append(f"{a}->{b}")
                elif nums[i] + 1 != nums[i+1] and nums[i+1] + nums[i+2] != nums[i+2]:
                    ans.append(f"{nums[i+1]}")
            except IndexError:
                break

        return ans

             
nums = [0,1,2,3,4,5,7,8]

sol = Solution()
ans = sol.summaryRanges(nums)
print(ans) ##################################   PENDING