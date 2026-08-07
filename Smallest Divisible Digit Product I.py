class Solution:
    def smallestDivisibleDigitProductI(self, n:int, t:int) -> int:

        

        ans = n


        product = 1

        

        if product % t == 0:
            return n


        for i in range(t):
            for i in str(ans):
                product *= int(i)
            if product % t == 0:
                return ans
            else:
                ans += 1

            product = 1



n = 1
t = 6

sol = Solution()
ans = sol.smallestDivisibleDigitProductI(n, t)
print(ans)