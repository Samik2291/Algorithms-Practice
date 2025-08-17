class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, sub = 0, []
        for char in s:
            sub.append(char)
            sub_set = set(sub)
            if len(sub) != len(sub_set):
                max_len = max(max_len, len(sub_set))
                index = sub.index(char) + 1
                sub = sub[index:]
        return max(max_len, len(sub))