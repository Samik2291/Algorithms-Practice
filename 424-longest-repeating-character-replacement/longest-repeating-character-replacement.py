class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq_dict = defaultdict(int)
        left = 0
        ret = 0
        max_freq = 0
        for right, val in enumerate(s):
            freq_dict[val] += 1
            max_freq = max(max_freq, freq_dict[val])
            curr_len = right - left + 1
            if curr_len - max_freq > k:
                freq_dict[s[left]] -= 1
                left += 1
            ret = max(ret, right - left + 1)
        return ret

            


        
            
            
