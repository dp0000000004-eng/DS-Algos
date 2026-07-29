
class Solution:
    def bestTimeToBuyAndSellII(self, prices:list[int]) -> int:

        min_number = float('inf')
        max_profit = 0
        buy = 0
        sell = 0

        for i in range(len(prices)):
            if prices[i] < min_number:
                min_number = prices[i]

            elif prices[i] > min_number:
                buy = min_number
                for i in range(i, len(prices)):
                    if prices[i] > buy:
                        continue
                    elif prices[i] < buy:
                        sell = prices[i-1]
                        max_profit += sell - buy

            return max_profit
        



nums = [2,9, 1]
sol = Solution()
ans = sol.bestTimeToBuyAndSellII(nums)
print(ans)