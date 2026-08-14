class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subSet = set()

        l = 0

        maxi = 0

        for r in range(len(s)):
            while s[r] in subSet:
                subSet.remove(s[l])
                l += 1
            
            subSet.add(s[r])
            maxi = max(maxi, (r - l) + 1)
        
        return maxi
