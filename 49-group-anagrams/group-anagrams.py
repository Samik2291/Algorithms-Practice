class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sort_dict = defaultdict(list)
        for wrd in strs:
            sorted_wrd = "".join(sorted(list(wrd)))
            sort_dict[sorted_wrd].append(wrd)
        return list(sort_dict.values())
        