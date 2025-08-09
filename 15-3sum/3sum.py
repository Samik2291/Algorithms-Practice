class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = set()
        n, z, p = [], [], []
        for num in nums:
            if num == 0:
                z.append(num)
            elif num < 0:
                n.append(num)
            else:
                p.append(num)
        
        n_set, p_set = set(n), set(p)
        if z:
            for num in p_set:
                neg = num * -1
                if neg in n_set:
                    ret.add((neg, 0, num))
        

        if len(z) > 2:
            ret.add((0, 0, 0))
        
        for first, second in combinations(n, 2):
            target = (first + second) * -1
            if target in p_set:
                ret.add(tuple(sorted([first, second, target])))
        for first, second in combinations(p, 2):
            target = (first + second) * -1
            if target in n_set:
                ret.add(tuple(sorted([first, second, target])))

        return [list(lst) for lst in ret]