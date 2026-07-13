class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        
        sortest_path = 0
        small = float('inf')

        for nums in triangle:
            s = 0
            for i in range(s, (len(nums))):
                if nums[i] < small:
                    small = nums[i]
            
            s = nums.index(small)
            sortest_path += small
            small = float('inf')

        return sortest_path
    
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

sol = Solution()
ans = sol.minimumTotal(triangle)
print(ans)