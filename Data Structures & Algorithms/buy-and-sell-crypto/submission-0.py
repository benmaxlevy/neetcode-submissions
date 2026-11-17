class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0

        for right in range(len(prices)):
            currProfit = prices[right] - prices[left]
            while left < right and currProfit < 0:
                currProfit = prices[right] - prices[left]
                left += 1

            profit = max(profit, prices[right] - prices[left])

        print((left, right))

        return profit