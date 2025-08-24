class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid - 1
        if nums[start] == target:
            return start
        return -1

                

        