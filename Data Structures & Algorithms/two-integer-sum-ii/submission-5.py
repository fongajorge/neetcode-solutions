class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1

        for _ in range(len(numbers)):
            for _ in range(p2, len(numbers)):
                if numbers[p1] + numbers[p2] == target:
                    return [p1 + 1, p2 + 1]

                p2 += 1

            p1 += 1
            p2 = p1 + 1
            
        return []
            