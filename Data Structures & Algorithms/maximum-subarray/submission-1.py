class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = -1001
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            mx = max(mx, sum)

            if sum < 0:
                sum = 0
        
        return mx