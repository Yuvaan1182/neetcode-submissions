INF = 100000
class Solution:

    def solve(self, coin: int, amount: int, coins: List[n]) -> int:
        if coin == len(coins):
            return INF
        if amount < 0:
            return INF
        if amount == 0:
            return 0
        
        if coins[coin] <= amount:
            pick = self.solve(
                            coin, 
                            amount - coins[coin],
                            coins
                            )
            notPick = self.solve(
                            coin+1,
                            amount,
                            coins
                            )
            return min(1 + pick, notPick)
        
        return INF

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1






        