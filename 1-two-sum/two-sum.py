class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [index, num_dict[diff]]
            num_dict[num] = index