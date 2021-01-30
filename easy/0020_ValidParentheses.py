class Solution:

    def validParentheses_inside_out(self, s: str) -> bool:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''

        if len(s) % 2 != 0:
            return False
        else:
            while '()' in s or '[]' in s or '{}' in s:
                s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if s == '':
                return True
            else:
                return False

    def validParentheses_stack(self, s: str) -> bool:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mapping.values():
                stack.append(s)
            elif char in mapping.keys():
                if stack == [] or dict[char] != stack.pop()
                    return False
            else:
                return False
        return stack == []


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    s = '()'
    solution = Solution()
    answer = solution.validParentheses_stack(s)
    print(answer)

    s = '()[]{}'
    solution = Solution()
    answer = solution.validParentheses_stack(s)
    print(answer)

    s = '([)]'
    solution = Solution()
    answer = solution.validParentheses_stack(s)
    print(answer)

    s = '([])'
    solution = Solution()
    answer = solution.validParentheses_stack(s)
    print(answer)
