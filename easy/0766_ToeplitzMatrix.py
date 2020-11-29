class Solution:

    def isToeplitzMatrix_compare_two_rows(self, matrix: list) -> bool:
        '''
        Time Complexity = O(NxM)
        Space Complexity = O(1)
        '''
        for i in range(len(matrix) - 1):
            list_a = matrix[i]
            list_b = matrix[i + 1]
            j = 0
            while j < (len(list_a) - 1):
                if list_a[j] == list_b[j + 1]:
                    j += 1
                    continue
                else:
                    return False
        return True

    def isToeplitzMatrix_compare_top_left(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    solution = Solution()
    answer = solution.isToeplitzMatrix_compare_two_rows(matrix)
    print(answer)

    matrix = [[1]]
    solution = Solution()
    answer = solution.isToeplitzMatrix_compare_two_rows(matrix)
    print(answer)

    matrix = [[]]
    solution = Solution()
    answer = solution.isToeplitzMatrix_compare_two_rows(matrix)
    print(answer)

    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    solution = Solution()
    answer = solution.isToeplitzMatrix_compare_top_left(matrix)
    print(answer)

    matrix = [[1]]
    solution = Solution()
    answer = solution.isToeplitzMatrix_compare_top_left(matrix)
    print(answer)

    matrix = [[]]
    solution = Solution()
    answer = solution.isToeplitzMatrix_compare_top_left(matrix)
    print(answer)
