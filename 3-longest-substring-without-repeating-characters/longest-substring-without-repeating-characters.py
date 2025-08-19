class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, left, sub = 0, 0, set()
        for char in s:
            sub_len = len(sub)
            sub.add(char)
            if len(sub) == sub_len:
                max_len = max(max_len, len(sub))
                while s[left] != char:
                    sub.remove(s[left])
                    left += 1
                left += 1
        return max(max_len, len(sub))