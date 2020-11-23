import collections
import heapq


class Solution:

    def minStartValue(self, nums: list) -> int:
        i = 1
        while True:
            sum_ = self.loopSum(i, nums)
            if not sum_:
                i += 1
            else:
                return i

    def loopSum(self, sum_, nums):
        for j in range(len(nums)):
            sum_ = sum_ + nums[j]
            if sum_ < 1:
                return False
        else:
            return sum_


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [-3, 2, -3, 4, 2]

    solution = Solution()
    answer = solution.minStartValue(nums)
    print(answer)
