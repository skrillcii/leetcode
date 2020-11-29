class Solution:

    def sumZero_1st_trial(self, n: int) -> list:
        '''
         Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        list_ = []
        if n % 2 == 0:
            for i in range(n // 2):
                list_.append(i + 1)
                list_.append(-i - 1)
        else:
            for i in range(n // 2):
                list_.append(i + 1)
                list_.append(-i - 1)
            list_.append(0)
        return list_

    def sumZero_wave_out(self, n: int) -> list:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        return [i for i in range(1 - n, n, 2)]


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    n = 5
    solution = Solution()
    answer = solution.sumZero_1st_trial(n)
    print(answer)

    n = 3
    solution = Solution()
    answer = solution.sumZero_1st_trial(n)
    print(answer)

    n = 1
    solution = Solution()
    answer = solution.sumZero_1st_trial(n)
    print(answer)

    n = 5
    solution = Solution()
    answer = solution.sumZero_wave_out(n)
    print(answer)

    n = 3
    solution = Solution()
    answer = solution.sumZero_wave_out(n)
    print(answer)

    n = 1
    solution = Solution()
    answer = solution.sumZero_wave_out(n)
    print(answer)
