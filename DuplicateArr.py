
class Solution:
    def DuplicatNums(self, nums:list[int]) -> bool:
        nums.sort()

        # set_ = set()

        # for i in nums:
        #     if i in set_:
        #         return True
        #         break
        #     elif i not in set_:
        #         set_.add(i)
        # else:
        #     return False
        k = 1
        for i in range(len(nums)):
            try:
                if nums[i] == nums[k]:
                    return True
                else:
                    k += 1
            except IndexError:
                return False


nums = [1, 2, 3, 1]

sol = Solution()
ans = sol.DuplicatNums(nums)
print(ans)