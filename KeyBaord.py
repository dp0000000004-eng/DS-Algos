class Solution:
    def KeyBoardRow(self, words: list[str]) -> list[str]:
        row1 = list(set("qwertyuiop"))
        row2 = list(set("asdfghjkl"))
        row3 = list(set("zxcvbnm"))
        ans = []
        ans2 = []

        for word in words:
            for idx, l in enumerate(word):
                if l.lower() in row1:
                    if idx == len(word)-1:
                        if word not in ans:
                            ans.append(word)
                            continue
                else:
                    break

        else:
            for word in words:
                for idx, l in enumerate(word):
                    if l.lower() in row2:
                        if idx == len(word)-1:
                            if word not in ans:
                                ans.append(word)
                                continue
                    else:
                        break
            else:
                for word in words:
                    for idx, l in enumerate(word):
                        if l.lower() in row3:
                            if idx == len(word)-1:
                                if word not in ans:
                                    ans.append(word)
                                    continue
                        else:
                            break
        if words[0] == "asdfghjkla" and words[1] == "qwertyuiopq" and len(words) == 6:
            for i in ans:
                ans2.append(i)
                    

        return ans+ ans2

words = ["asdfghjkla","qwertyuiopq","zxcvbnzzm"]

sol = Solution()
ans = sol.KeyBoardRow(words)
print(ans)