class Solution:

    def heightChecker_sort_compare(self, heights: list) -> int:
        '''
        Time Complexity = (NlogN)
        Space Complexity = (N)
        '''
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

    def heightChecker_bucket_counting(self, heights: list) -> int:
        '''
        Time Complexity = (N)
        Space Complexity = (N)
        '''

        count = 0
        dict_ = [0] * 100
        sort_ = []
        for i, h in enumerate(heights):
            dict_[h] += 1

        for i in range(len(dict_)):
            sort_.extend([i for _ in range(dict_[i])])
        return sum(h1 != h2 for h1, h2 in zip(heights, sort_))


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    heights = [1, 1, 1, 4, 2, 1, 3]
    solution = Solution()
    answer = solution.heightChecker_bucket_counting(heights)
    print(answer)

    heights = [5, 1, 2, 3, 4]
    solution = Solution()
    answer = solution.heightChecker_bucket_counting(heights)
    print(answer)

    heights = [1, 2, 3, 4, 5]
    solution = Solution()
    answer = solution.heightChecker_bucket_counting(heights)
    print(answer)
