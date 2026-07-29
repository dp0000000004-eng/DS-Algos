class Solution:
    def validAnagram(self, s:str, t:str) -> bool:
        a = {}
        b = {}

        for i, w in enumerate(sorted(s)):
            a[i] = w
        for i, w in enumerate(sorted(t)):
            b[i] = w

        ans = True

        for i in range(len(s)):
            try:
                if a[i] == b[i]:
                    continue
                else:
                    ans = False
            except KeyError:
                ans = False
                break

        return ans



s = "bca"
t = "bcf"

sol = Solution()
ans = sol.validAnagram(s, t)
print(ans)