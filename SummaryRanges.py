class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        a = 0
        b = 0

        ans = []
        
        for i in range(len(nums)):
            try:
                if nums[i] + 1 == nums[i+1]:
                    a = nums[i]
                    b = nums[i+1]
                    ans.append(f"{a}->{b}")
            except IndexError:
                break

        return ans

                


nums = [0,1,2,4,5,7]

sol = Solution()
ans = sol.summaryRanges(nums)
print(ans)