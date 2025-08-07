class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        vals = freq_dict.values()
        max_lst = []
        for _ in range(k):
            max_lst.append(max(vals))
            vals.pop(vals.index(max(vals)))
        ret_lst = []
        for key in freq_dict:
            if freq_dict[key] in max_lst:
                ret_lst.append(key)
        return ret_lst


        