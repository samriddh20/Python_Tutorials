def two_sum(nums, target):
    num_map = {}
    
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in num_map:
            return [num_map[compliment], i], num_map
        
        num_map[num] = i

nums = [5, 4, 3, 2, 11]
target = 6

print(two_sum(nums, target))
