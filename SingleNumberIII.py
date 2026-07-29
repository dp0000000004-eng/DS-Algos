class Solution:
    def SingleNumberIII(self, nums:list[int] ) -> list[int]:
        nums.sort()
        ans = []
        k = 1
        i = 0

        for _ in range(len(nums)):
            try:
                if nums[i] == nums[k]:
                    i += 2
                    k += 2
                    continue
                else:
                    ans.append(nums[i])
                    i += 1
                    k += 1
            except IndexError:
                try:
                    ans.append(nums[i])
                except IndexError:
                    break
                break

        return ans

nums = [0,1,2,2, 3, 3]
sol = Solution()
ans = sol.SingleNumberIII(nums)
print(ans)