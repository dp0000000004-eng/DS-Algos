from collections import Counter

class Solution:
    def RemoveDuplicatesfromSortedArrayII(self, nums:list[int]) -> int:

        store = []
        ans = 0



        for i in range(2):
            store.append(nums[i])

        for i in range(len(nums)+2):
            try:
                if store[len(store)-1] != nums[i] or store[len(store)-2] != nums[i] :
                    store.append(nums[i])
                    
            except IndexError:
                ans = len(store)

        new_a = list((Counter(nums) - Counter(store)).elements())
        print(new_a)

        for val in new_a:
            if val in nums:
                nums.remove(val)



        print(store)
        print(nums)

            
            
        return ans




nums = [ 1, 2, 2, 2, 3, 4, 4, 4]

sol = Solution()
ans = sol.RemoveDuplicatesfromSortedArrayII(nums)
print(ans)