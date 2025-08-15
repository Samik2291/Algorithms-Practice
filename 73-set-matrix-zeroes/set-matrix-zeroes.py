class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for row_indx in range(len(matrix)):
            for col_indx in range(len(matrix[row_indx])):
                if matrix[row_indx][col_indx] == 0:
                    rows.append(row_indx)
                    cols.append(col_indx)
        '''
        for row_indx in range(len(matrix)):
            if row_indx in rows:
                for col_indx in range(len(matrix[row])):
                    matrix[row_indx][col_indx] = 0
        '''
        for row_indx in range(len(matrix)):
            for col_indx in range(len(matrix[row_indx])):
                if col_indx in cols or row_indx in rows:
                    matrix[row_indx][col_indx] = 0


        