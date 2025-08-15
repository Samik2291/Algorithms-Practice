class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        rows, cols = len(matrix), len(matrix[0])
        right, left, top, bot = cols, 0, 0, rows
        while len(ret) < rows*cols:
            #top row
            for num in matrix[top][left:right]:
                ret.append(num)
            top += 1

            #right col
            for index in range(top, bot-1):
                lst = matrix[index]
                ret.append(lst[right-1])

            #bot row
            for num in reversed(matrix[bot-1][left:right]):
                ret.append(num)
            bot -= 1

            # left col
            for index in range(bot-1, top-1, -1):
                lst = matrix[index]
                ret.append(lst[left])

            right -= 1
            left += 1

        return ret[:rows*cols]
        