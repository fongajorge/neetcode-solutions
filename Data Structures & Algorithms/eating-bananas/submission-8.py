# Binary Search
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) + 1

        currentMin = max(piles) + 2

        while l <= r:
            m = (l + r) // 2

            dummy = piles.copy()
            hours = 0

            for element in dummy:
                hours += -(-element // m)

            if hours <= h:
                if m < currentMin:
                    currentMin = m
                
                r = m - 1
            else:
                l = m + 1

        return currentMin
