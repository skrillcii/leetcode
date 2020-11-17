class Solution:

    def numIslands(self, grid:list):
        """
        :type grid: List[List[str]]
        :rtype: int
        """


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [[1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            ]

    solution = Solution()
    answer = solution.numIslands(nums)
    print(answer)
