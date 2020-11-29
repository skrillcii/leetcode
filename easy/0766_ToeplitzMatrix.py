class Solution:

    def toeplitzMatix(self, matrix: list) -> bool:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
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


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    solution = Solution()
    answer = solution.toeplitzMatix(matrix)
    print(answer)

    matrix = [[1]]
    solution = Solution()
    answer = solution.toeplitzMatix(matrix)
    print(answer)

    matrix = [[]]
    solution = Solution()
    answer = solution.toeplitzMatix(matrix)
    print(answer)
