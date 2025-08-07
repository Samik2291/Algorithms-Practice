class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev_prod = {}
        prod = 1
        for index in range(len(nums)):
            prev_prod[index] = prod
            prod *= nums[index]
        after_prod = {}
        prod = 1
        for index in range(len(nums)-1, -1, -1):
            after_prod[index] = prod
            prod *= nums[index]
        
        answ = []
        for index in range(len(nums)):
            answ.append(prev_prod[index] * after_prod[index])
        return answ
        

        