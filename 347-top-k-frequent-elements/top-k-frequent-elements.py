class Solution(object):
    def topKFrequent(self, nums, k):
        """
        num_to_freq = {}
        for num in nums:
            if num in num_to_freq:
                num_to_freq[num] += 1
            else:
                num_to_freq[num] = 1

        freq_to_num = {}
        for num in num_to_freq:
            freq = num_to_freq[num]
            if freq in freq_to_num:
                freq_to_num[freq].append(num)
            else:
                freq_to_num[freq] = [num]

        freq_lst = []
        for freq in range(len(nums), 0, -1):
            if freq in freq_to_num:
                freq_lst.extend(freq_to_num[freq])
        
        return freq_lst[:k]
        """
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]
        