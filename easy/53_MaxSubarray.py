class Solution:

    def maxSubArray(self, nums: list) -> int:

        import ipdb
        ipdb.set_trace()

        output = []
        if len(nums) == 1:
            output = nums

        sum_ = []
        for idx in range(len(nums)):
            if idx == 0:
                sum_.append(nums[idx])
            else:
                cur_value = nums[idx]
                sum_with_prev = cur_value + sum_[idx - 1]
                sum_.append(max([cur_value, sum_with_prev]))
        output = max(sum_)
        return output


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    solution = Solution()
    answer = solution.maxSubArray(x)
    print(answer)
