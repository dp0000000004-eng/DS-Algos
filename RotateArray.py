def call():
    nums = [1,2,3,4,5,6,7]
    nums1 = []

    def inner():
        nonlocal nums, nums1

        for i in nums:
            nums1.append(i)

        for i in range(len(nums)):
            try:
                nums[i+1] = nums1[i]
            except IndexError:
                nums[0] = nums1[i]
        
        for i in range(len(nums)):
            nums1[i] = nums[i]
        
        print("nums:", nums)
        print("nums1:", nums1)

    return inner   # return the function itself

# Create a persistent function
f = call()

for i in range(3):
    f()