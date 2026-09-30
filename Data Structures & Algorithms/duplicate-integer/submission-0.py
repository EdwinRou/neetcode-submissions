class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for number in nums:
            if number in num_dict:
                return True
            else:
                num_dict[number] = None
        return False
        
        