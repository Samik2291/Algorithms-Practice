class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index in range(len(nums)):
            goal = target - nums[index]
            if goal in nums_dict:
                return [nums_dict[goal], index]
            nums_dict[nums[index]] = index
