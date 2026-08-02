class Solution:
    def productExceptSelf(self, nums: list[int]) -> list(int):
        answer = [1] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)):
            answer[-i - 1] *= suffix
            suffix *= nums[-i - 1]

        return answer