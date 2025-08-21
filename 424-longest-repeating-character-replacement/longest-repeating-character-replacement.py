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
        for right in range(len(s)):
            freq_dict[s[right]] += 1
            curr_len = right - left + 1
            max_freq = max(freq_dict.values())
            if curr_len - max_freq > k:
                freq_dict[s[left]] -= 1
                left += 1
            ret = max(ret, right - left + 1)
        return ret

            


        
            
            
