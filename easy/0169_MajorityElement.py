class Solution:

    def majorityElement_hash_map(self, nums: list) -> int:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''

        if nums == []:
            return 0

        dict_ = dict()
        for i in nums:
            if i not in dict_.keys():
                dict_[i] = 1
            else:
                dict_[i] += 1

        return max(dict_, key=dict_.get)

    def majorityElement_count_otherwise(self, nums: list) -> int:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        major = nums[0]
        count = 0
        for num in nums:
            if num == major:
                count += 1
            else:
                count -= 1
            if count < 0:
                major = num
                count = 1
        return major


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [3, 2, 3]
    solution = Solution()
    answer = solution.majorityElement_hash_map(nums)
    print(answer)

    nums = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    answer = solution.majorityElement_hash_map(nums)
    print(answer)

    nums = [6, 5, 5]
    solution = Solution()
    answer = solution.majorityElement_hash_map(nums)
    print(answer)

    nums = [3, 2, 3]
    solution = Solution()
    answer = solution.majorityElement_count_otherwise(nums)
    print(answer)

    nums = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    answer = solution.majorityElement_count_otherwise(nums)
    print(answer)

    nums = [6, 5, 5]
    solution = Solution()
    answer = solution.majorityElement_count_otherwise(nums)
    print(answer)
