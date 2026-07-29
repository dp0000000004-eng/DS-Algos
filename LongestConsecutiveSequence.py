class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)

        longest = 0
        current = 0


        for i in range(len(nums)):
            try:
                if nums[i] + 1== nums[i + 1] :
                    current  += 1
                    longest = max(current, longest)
                elif nums[i] == nums[i+1]:
                    continue
                else:
                    current = 1

            except IndexError:
                if current != longest:
                    longest += 1
                break

        return longest


nums = [9,1,4,7,3,-1,0,5,8,-1,6]


sol = Solution()
ans = sol.longestConsecutive(nums)
print(ans)