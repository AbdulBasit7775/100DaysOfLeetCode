class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i , num in enumerate(nums):
            complement = target - nums[i]
            if complement in result:
                return([result[complement],i])
            else:
                result[num] = i 
        
        return []