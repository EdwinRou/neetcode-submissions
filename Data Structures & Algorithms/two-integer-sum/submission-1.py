class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def check(nums, target, index):
            target = target - nums[index]
            for k in range(index+1, len(nums)):
                if k!= index:
                    if nums[k] == target:
                        return (True, [index,k])
            return False, None
        
        for i in range(len(nums)-1):
            result = check(nums, target, i)
            if result[0] == True :
                return result[1]
        

