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
            if height[start] > height[end]:
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else:
                start += 1
                end -= 1
        return area


        