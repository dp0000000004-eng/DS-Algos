class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:

            break_point = 0
            postion_of_bp = 0

            last = len(nums)-1
            p_last = len(nums)-2

            for _ in range(len(nums)):

                if nums[p_last] < nums[last]:
                    break_point = nums[last]
                    postion_of_bp = last
                    break
                else:
                    last -= 1
                    p_last -= 1
            temp_array = []

            swap = 0

            for i in range(postion_of_bp, len(nums)):
                temp_array.append(nums[i])

            for num in sorted(temp_array):
                
                if num > nums[postion_of_bp-1]:
                    swap = num
                    break
            nums[nums.index(swap)] = nums[postion_of_bp-1]
            nums[postion_of_bp-1] = swap
            

            nums[postion_of_bp:] = sorted(nums[postion_of_bp:])

            print(break_point, postion_of_bp)

            print(nums)
        else:
            print(nums)
            pass


        

nums = [5,4,7,5,3,2]

sol = Solution()
ans = sol.nextPermutation(nums)