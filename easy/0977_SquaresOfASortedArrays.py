class Solution:

    def sortedSquares(self, A: list) -> list:
        '''
        Time Complexity = (N)
        Space Complexity = (N)
        '''
        list_ = []

        if A == []:
            return list_

        for i in A:
            list_.append(i * i)
        list_.sort()
        return list_


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    A = [-4, -1, 0, 3, 10]
    solution = Solution()
    answer = solution.sortedSquares(A)
    print(answer)
