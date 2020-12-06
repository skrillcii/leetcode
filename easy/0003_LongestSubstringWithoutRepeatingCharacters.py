class Solution:

    def lengthOfLongestSubstring_two_pointer_tracking(self, s: str) -> int:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        pointer1 = 0
        pointer2 = 0
        max_length = 0
        chars = {}

        for idx, char in enumerate(s):
            pointer2 = idx
            if char in chars and pointer1 <= chars[char]:
                pointer1 = chars[char] + 1
            max_length = max(max_length, pointer2 - pointer1 + 1)
            chars[char] = idx
        return max_length


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    s = 'abcabcbb'
    solution = Solution()
    answer = solution.lengthOfLongestSubstring_two_pointer_tracking(s)
    print(answer)

    s = 'bbbbb'
    solution = Solution()
    answer = solution.lengthOfLongestSubstring_two_pointer_tracking(s)
    print(answer)

    s = 'pwwkew'
    solution = Solution()
    answer = solution.lengthOfLongestSubstring_two_pointer_tracking(s)
    print(answer)

    s = ''
    solution = Solution()
    answer = solution.lengthOfLongestSubstring_two_pointer_tracking(s)
    print(answer)

    s = 'abba'
    solution = Solution()
    answer = solution.lengthOfLongestSubstring_two_pointer_tracking(s)
    print(answer)
