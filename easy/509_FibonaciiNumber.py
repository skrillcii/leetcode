class Solution:

    def fib_recursion(self, N: int) -> int:
        '''
        Time Complexity = (2^N)
        Space Complexity = (N)
        '''
        if N == 0 or N == 1:
            return N
        else:
            return self.fib_recursion(N - 1) + self.fib_recursion(N - 2)

    def fib_bottom_up(self, N: int) -> int:
        '''
        Time Complexity = (N)
        Space Complexity = (N)
        '''
        if N == 0 or N == 1:
            return N
        else:
            fib_seq = [0, 1]
            for i in range(2, N + 1):
                fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
            return fib_seq[N]

    def fib_iter_space_optimized(self, N: int) -> int:
        '''
        Time Complexity = (N)
        Space Complexity = (1)
        '''
        if N == 0 or N == 1:
            return N
        else:
            fib_seq = [0, 1]
            for _ in range(2, N + 1):
                fib_seq = [fib_seq[-1], fib_seq[-1] + fib_seq[-2]]
            return fib_seq[-1]

    def fib_iter_space_optimized_tuple(self, N: int) -> int:
        '''
        Time Complexity = (N)
        Space Complexity = (1)
        '''
        if N == 0 or N == 1:
            return N
        else:
            fib_seq = (0, 1)
            for _ in range(2, N + 1):
                fib_seq = (fib_seq[-1], fib_seq[-1] + fib_seq[-2])
            return fib_seq[-1]

    def fib_golden_ratio(self, N):
        '''
        Time Complexity = (1)
        Space Complexity = (1)
        '''
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)


if __name__ == '__main__':

    # import ipdb
    # ipdb.set_trace()

    # N = 2
    N = 30

    solution = Solution()
    answer = solution.fib_recursion(N)
    print(answer)
    answer = solution.fib_bottom_up(N)
    print(answer)
    answer = solution.fib_iter_space_optimized(N)
    print(answer)
    answer = solution.fib_iter_space_optimized_tuple(N)
    print(answer)
    answer = solution.fib_golden_ratio(N)
    print(answer)
