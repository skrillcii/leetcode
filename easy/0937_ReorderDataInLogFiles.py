class Solution:

    def reorderLogFiles(self, s: list) -> list:

        list_alpha = []
        list_numeric = []
        numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Split alpha & numeric
        for log in s:
            id_, words = log.split(' ', 1)
            if words[0] in numeric:
                list_numeric.append(log)
            else:
                list_alpha.append(log)

        # Sort alpha
        groups = {}
        for log in list_alpha:
            id_, words = log.split(' ', 1)
            if str(words) not in groups.keys():
                groups[str(words)] = [log]
            else:
                groups[str(words)].append(log)

        keys = sorted([i for i in groups.keys()])
        list_alpha = []
        for key in keys:
            if len(groups[key]) > 1:
                groups[key].sort(key=lambda x: x.split(' ')[0])
                list_alpha += groups[key]
            else:
                list_alpha += groups[key]

        return list_alpha + list_numeric


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    s = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    s = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    s = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]
    solution = Solution()
    answer = solution.reorderLogFiles(s)
    print(answer)
