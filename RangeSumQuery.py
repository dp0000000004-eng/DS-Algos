class NumArray:

    def __init__(self, nums:list[int]):
        
        self.nums = nums[0][0]
        self.ans = 0

        k = 1

        for i in range(len(self.nums)-1):
            self.left = nums[i+k][0]
            self.right = nums[i+k][1]
            k += 1
            break
        

    def sumRange(self, left: int, right: int) -> int:
        for i in range(left, right):
            self.ans +=  self.nums[i] + self.nums[i+1]
            
        return self.ans

nums = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

arry = NumArray(nums)

print(arry)
ans = arry.sumRange(0, 1)
print(ans)