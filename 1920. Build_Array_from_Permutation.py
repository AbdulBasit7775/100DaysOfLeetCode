def buildArray(self, nums: List[int]) -> List[int]:
        updated_list = []
        length = len(nums);
        for num in range(length):
            updated_list.append(nums[nums[num]])
        return updated_list