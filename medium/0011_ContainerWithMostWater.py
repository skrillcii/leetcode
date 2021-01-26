class Solution:

    def maxArea(self, height: list) -> int:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''

        if len(height) == 2:
            return self.calArea(min(height), 1)

        pointer1 = 0
        pointer2 = len(height) - 1
        max_area = 0

        while pointer1 != pointer2:
            area = self.calArea(min(height[pointer1], height[pointer2]), pointer2 - pointer1)
            if area > max_area:
                max_area = area

            if height[pointer1] <= height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return max_area

    def calArea(self, height: int, width: int) -> int:
        return height * width


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    answer = solution.maxArea(height)
    print(answer)

    height = [1, 1]
    solution = Solution()
    answer = solution.maxArea(height)
    print(answer)

    height = [4, 3, 2, 1, 4]
    solution = Solution()
    answer = solution.maxArea(height)
    print(answer)

    height = [1, 2, 1]
    solution = Solution()
    answer = solution.maxArea(height)
    print(answer)
