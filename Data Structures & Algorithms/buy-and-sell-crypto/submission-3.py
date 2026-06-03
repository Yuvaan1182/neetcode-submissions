class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mxP = 0
        sp = prices[n-1]

        # range(start, stop, step)
        for i in range(n-2, -1, -1):
            if prices[i] > sp:
                sp = prices[i]
            else:
                profit = sp - prices[i]
                mxP = max(profit, mxP)

        return mxP
        