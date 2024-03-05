class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for num in range(length):
            nums.append(nums[num])
        return nums
        