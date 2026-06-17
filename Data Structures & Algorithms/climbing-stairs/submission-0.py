class Solution:
    def solve(self, n: int, dp: List[int]) -> int:
        if n < 0: return 0
        if n == 0: return 1
        if dp[n] != -1: return dp[n]

        dp[n] = self.solve(n-1, dp) + self.solve(n-2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.solve(n, dp)