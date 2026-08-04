class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        visited = set()
        starts = []

        for n in nums:
            visited.add(n)

        for n in nums:
            if not n - 1 in visited:
                starts.append(n)

        longest = 1
        for n in starts:
            count = 1

            while n + 1 in visited:
                count += 1
                n += 1

                if count > longest:
                    longest = count

        return longest

            
            