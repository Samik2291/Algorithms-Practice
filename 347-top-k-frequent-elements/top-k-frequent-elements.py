class Solution(object):
    def topKFrequent(self, nums, k):
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
            if len(freq_lst) > k:
                break
        
        return freq_lst[:k]