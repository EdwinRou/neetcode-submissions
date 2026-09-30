class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            num_i = nums[i]
            for j in range(i+1,n):
                num_j = nums[j]
                sum_ij = num_i + num_j
                if target == sum_ij:
                    return [i, j]
        return None