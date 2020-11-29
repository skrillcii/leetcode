class Solution:

    def minTimeToVistAllPoints(self, points):
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        total = 0
        for i in range(len(points) - 1):
            total += max(abs(points[i][0] - points[i + 1][0]),
                         abs(points[i][1] - points[i + 1][1]))
        return total


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    points = [[1, 1], [3, 4], [-1, 0]]
    solution = Solution()
    answer = solution.minTimeToVistAllPoints(points)
    print(answer)
    # output 7

    points = [[3, 2], [-2, 2]]
    solution = Solution()
    answer = solution.minTimeToVistAllPoints(points)
    print(answer)
    # output 5
