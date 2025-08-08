class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod_dict = {}
        prod = 1
        for index, num in enumerate(nums):
            prod_dict[index] = prod
            prod *= num
        prod = 1
        for index in range(len(nums)-1, -1, -1):
            prod_dict[index] *= prod
            prod *= nums[index]
        
        return prod_dict.values()
        

        