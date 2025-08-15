class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = []
        zero_row = [0] * len(matrix[0])
        cols = []
        for row_indx in range(len(matrix)):
            for col_indx in range(len(matrix[row_indx])):
                if matrix[row_indx][col_indx] == 0:
                    rows.append(row_indx)
                    cols.append(col_indx)
        for row_indx in range(len(matrix)):
            if row_indx in rows:
                matrix[row_indx] = zero_row
            for col_indx in range(len(matrix[row_indx])):
                if col_indx in cols:
                    matrix[row_indx][col_indx] = 0


        