def missingNumber(self, nums: List[int]) -> int:
    length = len(nums)
    actual_sum = sum(nums)
    expected_sum = (length * (length+1))/2
    number = round(expected_sum - actual_sum)
    return number 