class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #prod_dict = {}
        prod_lst = []
        prod = 1
        for index, num in enumerate(nums):
            #prod_dict[index] = prod
            prod_lst.append(prod)
            prod *= num
        prod = 1
        for index in range(len(nums)-1, -1, -1):
            prod_lst[index] *= prod
            prod *= nums[index]
        
        return prod_lst
        

        