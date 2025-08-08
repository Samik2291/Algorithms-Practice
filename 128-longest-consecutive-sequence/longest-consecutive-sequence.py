class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_count = 1
        for num in nums:
            if num - 1 not in nums:
                nxt = num
                while nxt + 1 in nums:
                    nxt += 1
                max_count = max(max_count, nxt - num + 1)
        max_count = 0 if len(nums) == 0 else max_count
        return max_count



                


            
