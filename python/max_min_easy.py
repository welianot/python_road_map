nums =[23,12,89,45,22]
nums.sort()
print(nums)
print(f"The max number is {nums[-1]} which is at index {nums.index(nums[-1])}")
print(f"The min number is {nums[0]} which is at index {nums.index(nums[0])}")
print(f"The second max number is {nums[-2]} which is at index {nums.index(nums[-2])}")
print(f"The second min number is {nums[1]} which is at index {nums.index(nums[1])}")