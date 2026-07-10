# class Solution:
#     def jumpGame(self, nums:list[int]) -> bool:

#         ans = False
#         try:
#             for i in range(len(nums)):
#                 if len(nums) >= 2:
#                     if nums[i+1] == 1 and nums[i]  ==0:
#                         ans = False
#                     elif (len(nums)-1) - i <= nums[i]:

#                         if (len(nums)-1) != i:
#                             ans = True
#                             break

#             if len(nums) == 1:
#                 ans = True
#         except AllError_That_Gonna_Happen:
#             return ans = CORRECT_ANS
        

#         return ans
                
            

# nums = [1, 2]

# sol = Solution()
# ans = sol.jumpGame(nums)
# print(ans)