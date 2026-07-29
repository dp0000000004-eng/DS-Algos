from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, nums: Optional[ListNode]) -> Optional[ListNode]:

        prev = None

        while nums:
            nxt = nums.next
            nums.next = prev
            prev = nums
            nums = nxt

        return nums

nums = [1,2,3]

sol = Solution()
ans = sol.reverseList(nums)
print(ans)