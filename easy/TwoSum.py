def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    unique = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff not in unique:
            unique[num] = i
        else:
            return [unique[diff], i]

if __name__ == '__main__':
    nums = [3,3]
    target = 6
    solution = twoSum(nums, target)
    print(solution)

