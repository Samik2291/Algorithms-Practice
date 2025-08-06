class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sort_dict = {}
        for wrd in strs:
            sorted_wrd = "".join(sorted(list(wrd)))
            if sorted_wrd in sort_dict:
                sort_dict[sorted_wrd].append(wrd)
            else:
                sort_dict[sorted_wrd] = [wrd]
        return list(sort_dict.values())
        