class Solution:

    def longestpalindrome(self, s: str) -> str:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''

        max_string = s[0]
        dict_ = {}
        for idx, char in enumerate(s):
            if char not in dict_.keys():
                dict_[char] = idx
            else:
                sub_string = s[dict_[char]:idx + 1]
                if len(sub_string) > len(max_string):
                    max_string = sub_string
        return max_string


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    s = 'babad'
    solution = Solution()
    answer = solution.longestpalindrome(s)
    print(answer)

    s = 'cbbd'
    solution = Solution()
    answer = solution.longestpalindrome(s)
    print(answer)

    s = 'a'
    solution = Solution()
    answer = solution.longestpalindrome(s)
    print(answer)

    s = 'ac'
    solution = Solution()
    answer = solution.longestpalindrome(s)
    print(answer)
