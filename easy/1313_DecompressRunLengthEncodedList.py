class Solution:

    def decompressRLElist(self, nums: list) -> list:
        '''
        Time Complexity = (N)
        Space Complexity = (N)
        '''
        if nums == []:
            return []

        list_ = []
        for i in range(len(nums) // 2):
            freq = nums[2 * i]
            val = nums[2 * i + 1]
            sub_list = [val] * freq
            list_.extend(sub_list)
        return list_


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [1, 2, 3, 4]
    solution = Solution()
    answer = solution.decompressRLElist(nums)
    print(answer)

    nums = [1, 1, 2, 3]
    solution = Solution()
    answer = solution.decompressRLElist(nums)
    print(answer)
