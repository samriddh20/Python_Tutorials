class Solution:
    def ProductExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1]*n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix *= nums[i]
        
        return answer

s = Solution()
print(s.ProductExceptSelf([1, 2, 3, 4]))
