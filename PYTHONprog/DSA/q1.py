# def two_sum(nums, target):
#     num_map = {}
    
#     for i, num in enumerate(nums):
#         compliment = target - num
#         if compliment in num_map:
#             return [num_map[compliment], i], num_map
        
#         num_map[num] = i

# nums = [5, 4, 3, 2, 11]
# target = 6

# print(two_sum(nums, target))

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         self.nums = nums
#         self.target = target
#         self.num_map = {}

#         for i, num in enumerate(self.nums):
#             compliment = target - num
#             if compliment in self.num_map:
#                 return [self.num_map[compliment], i]
#             self.num_map[num] = i

# nums = input("Enter your list of numbers: ")
# tgt = int(input("Enter the target number: "))        

# s = Solution()
# s.twoSum(nums, tgt)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


if __name__ == '__main__':
    # Interactive: enter numbers separated by spaces or commas, or press Enter to use the sample
    demo_input = input("Enter numbers separated by spaces or commas (or press Enter to use sample): ")
    if demo_input.strip():
        # allow both commas and spaces as separators
        demo_input = demo_input.replace("[", "").replace("]", "")
        nums = [int(x) for x in demo_input.replace(',', ' ').split() if x.strip()]
        tgt = int(input("Enter the target number: "))
        s = Solution()
        print(s.twoSum(nums, tgt))
        print(nums)
    else:
        # run a quick sample so the script is non-interactive for quick tests
        sample = [5, 4, 3, 2, 11]
        target = 6
        print("Using sample:", sample, "target:", target)
        print("Result:", Solution().twoSum(sample, target))
