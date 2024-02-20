class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 1;
        current_num = nums[0]
        for num in nums[1:]:
            if num != current_num:
                current_num = num
                nums[unique_count] = num
                unique_count += 1

        return unique_count