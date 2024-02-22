
def majorityElement(self, nums: List[int]) -> int:
candidate = None
count = 0
length = len(nums)
for num in range(length):
    if count == 0:
        candidate = nums[num]
        count = 1
    elif nums[num] == candidate:
        count += 1
    else:
        count -= 1
return candidate
