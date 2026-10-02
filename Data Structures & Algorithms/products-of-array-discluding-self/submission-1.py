class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0 for i in range(n)]
        total = 1
        zero_count = 0
        zero_index = None
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
                zero_index = i
                continue
            total *= nums[i]

        if zero_count > 1:
            return output
        if zero_count == 1:
            output[zero_index] = total
            return output
        else :
            for i in range(0,n):
                output[i] = total // nums[i]
        
        return output