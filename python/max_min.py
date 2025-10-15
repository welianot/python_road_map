nums =[23,12,89,45,22]
max_num=nums[0]
min_num=nums[0]

for nums in nums:
    if nums > max_num:
        max_num=nums
    if nums < min_num:
        min_num=nums

    
print(f"The max number is {max_num}")
print(f"The min number is {min_num}")