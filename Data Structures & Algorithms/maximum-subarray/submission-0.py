class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = -1001
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums), 1):
                sum += nums[j]
                mx = max(mx, sum)
        
        return mx