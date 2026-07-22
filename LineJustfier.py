class Solution:
    def wordJustfile(self, words:list[str], maxWidth) -> list[str]:

        ans = []
        store = ""

        for word in words:
            word_length = len(word)
            if len(store) < maxWidth and len(store) + word_length <= maxWidth:

                store += word + " "
            else:
                s = store.rstrip()
                if len(s) < maxWidth:
                    ...
                ans.append(s)
                store = ""
                store += word + " "
        ans.append(store)
    
        
        return ans

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20


sol = Solution()
ans = sol.wordJustfile(words, maxWidth)
print(ans)