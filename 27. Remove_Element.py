class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replace_value = 0
        for num in range(len(nums)):
            if nums[num] == val:
                nums[num] = '_';
            else:
                nums[replace_value] = nums[num]
                replace_value += 1;
        return replace_value
        