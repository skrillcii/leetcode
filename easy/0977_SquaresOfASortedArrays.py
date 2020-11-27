class Solution:

    def sortedSquares_1st_trial(self, A: list) -> list:
        '''
        Time Complexity = (NlogN)
        Space Complexity = (N)
        '''
        list_ = []

        if A == []:
            return list_

        for i in A:
            list_.append(i * i)
        list_.sort()
        return list_


    def sortedSquares_two_pointers(self, A: list) -> list:
        '''
        Time Complexity = (N)
        Space Complexity = (N)
        '''
        list_ = []

        if A == []:
            return list_

        N = len(A) - 1
        i = 0
        j = 0

        for _i, a in enumerate(A):
            if a >= 0:
                j = _i - 1
                i = _i
                break

        while j >= 0 and i <= N:
            if A[j] ** 2 < A[i] ** 2:
                list_.append(A[j] ** 2)
                j -= 1
            elif A[j] ** 2 > A[i] ** 2:
                list_.append(A[i] ** 2)
                i += 1

        while j >= 0:
            list_.append(A[j] ** 2)
            j -= 1

        while i <= N:
            list_.append(A[i] ** 2)
            i += 1

        return list_



if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    A = [-4, -1, 0, 3, 10]
    solution = Solution()
    answer = solution.sortedSquares_two_pointers(A)
    print(answer)
