class Solution:
    def keyBoard123(self, word:str) -> int:

        ans = 0
        k = 1

        
        for i in range( len(word)):
            if i+1 > 8:
                k = 2
            if i +1> 16:
                k = 3
            if i +1> 24:
                k = 4
            ans += k
            



        return ans



word = "abcdefghijklmnopqrstuvwx"

sol = Solution()
ans = sol.keyBoard123(word)
print(ans)