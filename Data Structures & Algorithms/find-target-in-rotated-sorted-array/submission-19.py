class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            print(f"l = {l}, m = {m}, r = {r}")

            if nums[m] == target:
                return m
            elif nums[m] > nums[r]: # El pivot esta a la derecha
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1
        