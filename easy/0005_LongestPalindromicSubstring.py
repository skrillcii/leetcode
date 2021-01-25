class Solution:

    def longestPalindrome(self, s: str) -> str:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''

        max_string = s[0]
        for idx in range(len(s)):
            # For odd length
            sub_string = self.subPalindrome(s, idx, idx)
            if len(sub_string) > len(max_string):
                max_string = sub_string
            # For even length
            sub_string = self.subPalindrome(s, idx, idx + 1)
            if len(sub_string) > len(max_string):
                max_string = sub_string
        return max_string

    def subPalindrome(self, s: str, j: int, k: int) -> str:
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        sub_string = s[j + 1:k]
        return sub_string


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    s = 'babad'
    solution = Solution()
    answer = solution.longestPalindrome(s)
    print(answer)

    s = 'cbbd'
    solution = Solution()
    answer = solution.longestPalindrome(s)
    print(answer)

    s = 'a'
    solution = Solution()
    answer = solution.longestPalindrome(s)
    print(answer)

    s = 'ac'
    solution = Solution()
    answer = solution.longestPalindrome(s)
    print(answer)

    s = 'aacabdkacaa'
    solution = Solution()
    answer = solution.longestPalindrome(s)
    print(answer)

    s = 'ccc'
    solution = Solution()
    answer = solution.longestPalindrome(s)
    print(answer)
