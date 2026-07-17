class Solution:
    def BaseballGame(self, board:list[str] ) -> int:

        stack = []
        
        for i in range(len(board)):
            token = board[i]
            
            try:
                val = int(token)
                stack.append(val)
            except ValueError:
                if token == "C":
                    if stack:
                        stack.pop()
                elif token == "D":
                    if stack:
                        stack.append(stack[-1] * 2)
                elif token == "+":
                    if len(stack) >= 2:
                        stack.append(stack[-1] + stack[-2])
                else:
                    continue

        return sum(stack)


nums = ["1","2","+","C","5","D"]

sol = Solution()
ans = sol.BaseballGame(nums)
print(ans)

