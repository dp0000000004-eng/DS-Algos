class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        if len(nums) > 2:

            last = len(nums)-1
            p_last = len(nums)-2

            for _ in range(len(nums)):
                if p_last == 0:
                    comp = nums[p_last]


                    if nums == sorted(nums, reverse=True):
                        nums.sort()
                        break

                    nums.sort()

                    l = None

                    for num in nums:
                        if num > comp:
                            l = num
                            break
                        

                    nums.remove(l)

                    nums.insert(0, l)

                    break


                elif nums[last] > nums[p_last]:
                    curr = nums[last]
                    nums[last] =  nums[p_last]
                    nums[p_last] = curr
                    break
                else:
                    last -= 1
                    p_last -= 1

        else:
            if len(nums) == 1:
                pass
            else:
                nums.reverse()
