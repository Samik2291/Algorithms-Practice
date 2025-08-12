class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        start, end = 0, len(height) - 1
        while start < end:
            area = max((min(height[start], height[end]) * (end - start)), area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return area


        