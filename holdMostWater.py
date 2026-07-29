class Solution:
    def holdMostWater(self, hights:list[int]) -> int:

        left = 0
        right = len(hights) - 1

        ans = 0

        while left < right:                  #Formula = min(hights[left], hights[right]) * (right - left)
            holding = min(hights[left], hights[right]) * (right - left)
            if holding > ans:
                ans = holding
            if hights[left] < hights[right]:
                left += 1
            else:
                right -= 1

        return ans


nums = [1,8,6,2,5,4,8,3,7]
sol = Solution()
ans = sol.holdMostWater(nums)
print(ans)