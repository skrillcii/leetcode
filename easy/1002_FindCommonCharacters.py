class Solution:

    def commonChars(self, A: list) -> list:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        ref = min(A, key=len)
        A.remove(ref)
        list_ = []
        for char in ref:
            bool_ = all([char in string for string in A])
            if bool_:
                list_.append(char)
                A = [string.replace(char, "", 1) for string in A]
        return list_


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    A = ["bella", "label", "roller"]
    solution = Solution()
    answer = solution.commonChars(A)
    print(answer)

    A = ["cool", "lock", "cook"]
    solution = Solution()
    answer = solution.commonChars(A)
    print(answer)
