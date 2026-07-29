nums = [2, 4, 1, 5]

min_number = float('inf')
max_profit = 0

for n in nums:
    if n < min_number:
        min_number = n
    elif n - min_number > max_profit:
        max_profit = n - min_number


print(max_profit)