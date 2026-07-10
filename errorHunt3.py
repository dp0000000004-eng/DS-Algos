nums = [3, 5, 4, 1,2, 8, 7]

day_of_sell = 3

sell= 0
sell_arr = []

for i in range(len(nums)-day_of_sell-1):
    sell_arr.append(nums[i + day_of_sell + 1])
    

sell = max(sell_arr)

print(sell_arr, sell)