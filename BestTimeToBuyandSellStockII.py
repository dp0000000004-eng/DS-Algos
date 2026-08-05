
class Solution:
    def bestTimeToBuyAndSellII(self, prices:list[int]) -> int:

        max_profit = 0

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                max_profit += prices[i+1] - prices[i]

        return max_profit



nums = [2,9, 1, 2 , 5, 1]
sol = Solution()
ans = sol.bestTimeToBuyAndSellII(nums)
print(ans)