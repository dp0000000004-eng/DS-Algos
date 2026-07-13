class NumArray:

    def __init__(self, nums: list[int]):

        self.ans = 0
        self.nums = nums
    

    def sumRange(self, left: int, right: int) -> int:

        for i in range(left, (right+1)):
            self.ans +=  self.nums[i]
            
        return self.ans


nums = [-2,0,3,-5,2,-1]
left = 2
right = 5

obj = NumArray(nums)
param_1 = obj.sumRange(left,right)
print(param_1)