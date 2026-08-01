class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            mult = 1

            for j in range(len(nums)):
                if i != j:
                    mult *= nums[j]
            
            answer.append(mult)

        return answer



        