class Solution:

    def validParentheses(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
        else:
            while '()' in s or '[]' in s or '{}' in s:
                s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if s == '':
                return True
            else:
                return False


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    s = '([])'

    solution = Solution()
    answer = solution.validParentheses(s)
    print(answer)
