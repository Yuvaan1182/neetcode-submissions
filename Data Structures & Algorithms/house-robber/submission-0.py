class Solution:

    def solve(self, i: int, nums: List[int], dp: List[int]) -> int:
        if i >= len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]
        
        pick = nums[i] + self.solve(i+2, nums, dp)
        notPick = self.solve(i+1, nums, dp)

        dp[i] = max(pick, notPick)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums)+1)
        return max(self.solve(0, nums, dp), self.solve(1, nums, dp))