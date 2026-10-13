class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = 0
        while right<len(prices):
            cur_p = prices[right]-prices[left]
            if cur_p>max_profit:
                max_profit = cur_p
            if prices[right]<prices[left]:
                left = right
            right+=1
        return max_profit