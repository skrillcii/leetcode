class Solution:

    def minimumAnsDifference_1st_trial(self, arr: list) -> list:
        '''
        Time Complexity = O(Nx(N-1))
        Space Complexity = O(N)
        '''
        min_ = None
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                diff = abs(arr[i] - arr[j])
                if min_ is None or diff < min_:
                    min_ = diff

        list_ = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                diff = abs(arr[i] - arr[j])
                if diff == min_:
                    list_.append(sorted([arr[i], arr[j]]))
        list_.sort()
        return list_

    def minimumAnsDifferenc_zipping(self, arr: list) -> list:
        '''
        Time Complexity = O(NlogN)
        Space Complexity = O(N)
        '''
        arr.sort()
        min_ = min([abs(a - b) for a, b in zip(arr[:-2], arr[1:])])
        return [[a, b] for a, b in zip(arr, arr[1:]) if abs(a - b) == min_]


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    arr = [4, 2, 1, 3]
    solution = Solution()
    answer = solution.minimumAnsDifference_1st_trial(arr)
    print(answer)

    arr = [1, 3, 6, 10, 15]
    solution = Solution()
    answer = solution.minimumAnsDifference_1st_trial(arr)
    print(answer)

    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    solution = Solution()
    answer = solution.minimumAnsDifference_1st_trial(arr)
    print(answer)

    arr = [4, 2, 1, 3]
    solution = Solution()
    answer = solution.minimumAnsDifferenc_zipping(arr)
    print(answer)

    arr = [1, 3, 6, 10, 15]
    solution = Solution()
    answer = solution.minimumAnsDifferenc_zipping(arr)
    print(answer)

    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    solution = Solution()
    answer = solution.minimumAnsDifferenc_zipping(arr)
    print(answer)
