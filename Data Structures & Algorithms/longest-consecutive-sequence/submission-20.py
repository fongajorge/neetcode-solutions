class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)

        longest = 0
        for n in visited:
            if n - 1 not in visited:
                count = 1

                while n + 1 in visited:
                    count += 1
                    n += 1

                longest = max(longest, count)
        
        return longest
        