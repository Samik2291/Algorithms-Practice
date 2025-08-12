class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area_lst = []
        start = 0
        end = len(height) - 1
        while start < end:
            area_lst.append(min(height[start], height[end]) * (end - start))
            if height[start] > height[end]:
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else:
                start += 1
                end -= 1
        return max(area_lst)


        