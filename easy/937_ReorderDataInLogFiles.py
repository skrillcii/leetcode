
class Solution:
    def reorderLogFiles(self, s: list) -> list:

        import ipdb
        ipdb.set_trace()

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
        sub_groups = {}
        for log in list_alpha:
            id_, words = log.split(' ', 1)
            if str(words[0]) not in sub_groups.keys():
                sub_groups[str(words[0])] = [log]
            else:
                sub_groups[str(words[0])].append(log)

        keys = sorted([i for i in sub_groups.keys()])
        list_alpha = []
        for key in keys:
            sub_groups[key].sort(key=lambda x: x[0])
            list_alpha += sub_groups[key]

        return list_alpha + list_numeric


if __name__ == '__main__':
    s = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    solution = Solution()
    answer = solution.reorderLogFiles(s)
    print(answer)
