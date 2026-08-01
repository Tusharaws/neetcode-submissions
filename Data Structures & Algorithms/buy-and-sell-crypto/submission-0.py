class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0

        for price in prices:
            while stack and price<stack[-1]:
                stack.pop()
            if stack:
                current_profit = price - stack[0]
                max_profit = max(max_profit, current_profit)
            stack.append(price)
        return max_profit
