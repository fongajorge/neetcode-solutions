class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        visited = set()

        for n in nums:
            visited.add(n)

        longest = 1
        for n in nums:
            if n - 1 not in visited:
                count = 1

                while n + 1 in visited:
                    count += 1
                    n += 1

                    if count > longest:
                        longest = count
        
        return longest