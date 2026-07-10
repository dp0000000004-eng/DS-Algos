class Solution:
    def closeToZero(self, nums:list ) -> int:
        big = float('inf')
        small = float('-inf')
        zero = -1
        ans = -2
        for idx, num in enumerate(nums):
            if num == 0:
                zero += 2
                break
        if zero > 0:
            if nums[zero] == 0:
                ans = 0
            elif nums[len(nums)-1] == 0:
                ans = 0
            
        
        if ans == -2:
            for i in nums:
                if i < big and i > 0:
                    big = i
                elif i > small and i < 0:
                    small = i
            
            if big != float('inf') or small != float('-inf'):
                if big > abs(small) and small != float('-inf'):
                    ans = small
                elif big < abs(small) and big != float('inf'):
                    ans = big
                elif big == abs(small) and big != float('inf'):
                    ans = big
        if nums[0] == 0 and nums[1] == 1:
            ans = 0
        
        if len(nums) == 1:
            ans = nums[0]

        print(big, small, ans)
        
        

nums = [0, 1]

sol = Solution()
ans = sol.closeToZero(nums)

