class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container_storages = []

        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                container_storages.append(min(heights[i], heights[j]) * (j - i))

        return max(container_storages)
        