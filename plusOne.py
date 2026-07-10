class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        k = len(digits) - 1
        if digits[k] >= 9:
            digits[k] = digits[k] + 1
        def arrPro(self, digits):
            for i in range(len(digits)):
                if digits[i] == 10:
                    digits[i] = digits[i] % 10
                    if digits[i-1] != 0 and 10:

                        digits[i-1] = digits[i-1] + 1
                    elif digits[i-1] == 0 and 10:
                        digits.insert(0, 1)
        for i in digits:
            if i == 10:
                arrPro(self, digits)
        return digits
digits = [1, 2, 4]

solution = Solution()
ans = solution.plusOne(digits)
print(ans)