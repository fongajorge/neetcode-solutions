class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxi = 0

        while r < len(prices):
            current = prices[r] - prices[l]

            if current > maxi:
                maxi = current

            elif prices[l] > prices[r]:
                l += 1
                r = l + 1
            else:
                r += 1
        
        return maxi
        