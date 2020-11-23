class Solution:

    def shuffleTheArray(self, nums: list, n: int) -> list:
        '''
        Time Complexity = (N) or (N/2)
        Space Complexity = (N)
        '''
        list_ = []
        for head1 in range(n):
            list_.append(nums[head1])
            list_.append(nums[head1+n])
        return list_


if __name__ == '__main__':

    # import ipdb
    # ipdb.set_trace()

    nums = [2, 5, 1, 3, 4, 7]
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    nums = [1, 1, 2, 2]

    solution = Solution()
    answer = solution.shuffleTheArray(nums, int(len(nums)/2))
    print(answer)
