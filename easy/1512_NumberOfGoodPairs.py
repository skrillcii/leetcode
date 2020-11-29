class Solution:

    def numIdenticalPairs_double_loop(self, nums: list) -> int:
        '''
        Time Complexity = O(Nx(N-1))
        Space Complexity = O(1)
        '''
        counter = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    counter += 1
        return counter

    def numIdenticalPairs_hash_table(self, nums: list) -> int:
        '''
        Time Complexity = O(Nx(N))
        Space Complexity = O(1)
        '''
        dict_ = dict()
        for num in nums:
            if num not in dict_.keys():
                dict_[num] = 0
            else:
                dict_[num] += 1
        return sum([self.__combinatiom(count) for count in dict_.values()])

    def __combinatiom(self, count):
        combinations = 0
        for i in range(count + 1):
            combinations += i
        return combinations


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [1, 2, 3, 1, 1, 3]
    solution = Solution()
    answer = solution.numIdenticalPairs_double_loop(nums)
    print(answer)

    nums = [1, 1, 1, 1]
    solution = Solution()
    answer = solution.numIdenticalPairs_double_loop(nums)
    print(answer)

    nums = [1, 2, 3]
    solution = Solution()
    answer = solution.numIdenticalPairs_double_loop(nums)
    print(answer)

    nums = [1, 2, 3, 1, 1, 3]
    solution = Solution()
    answer = solution.numIdenticalPairs_hash_table(nums)
    print(answer)

    nums = [1, 1, 1, 1]
    solution = Solution()
    answer = solution.numIdenticalPairs_hash_table(nums)
    print(answer)

    nums = [1, 2, 3]
    solution = Solution()
    answer = solution.numIdenticalPairs_hash_table(nums)
    print(answer)
