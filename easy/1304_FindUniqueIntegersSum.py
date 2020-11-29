class Solution:

    def sumZero(self, n: int) -> list:
        '''
         Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        list_ = []
        if n % 2 == 0:
            for i in range(n / 2):
                list_.append(i + 1)
                list_.append(-i - 1)
        else:
            for i in range(n // 2):
                list_.append(i + 1)
                list_.append(-i - 1)
            list_.append(0)
        return list_


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    n = 5
    solution = Solution()
    answer = solution.sumZero(n)
    print(answer)

    n = 3
    solution = Solution()
    answer = solution.sumZero(n)
    print(answer)

    n = 1
    solution = Solution()
    answer = solution.sumZero(n)
    print(answer)
