class Solution:

    def transpose_one_liner(self, A: list) -> list:
        '''
        Time Complexity = O(1)
        Space Complexity = O(MxN)
        '''
        return list(zip(*A))

    def transpose_list_comprehension(self, A):
        '''
        Time Complexity = O(MxN)
        Space Complexity = O(MxN)
        '''
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    answer = solution.transpose_one_liner(A)
    print(answer)

    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    answer = solution.transpose_list_comprehension(A)
    print(answer)
