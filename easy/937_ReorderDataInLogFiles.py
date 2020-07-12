
class Solution:
    def reorderLogFiles(self, s: list) -> list:

        list_alpha = []
        list_numeric = []
        numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for idx, log in enumerate(s):
            id_, words = log.split(' ', 1)
            if words[0] in numeric:
                list_numeric.append((id_, words))
            else:
                list_alpha.append((id_, words))

        list_numeric.sort(key=lambda x: x[1], reverse=True)
        list_alpha.sort(key=lambda x: x[1])

        sub_groups = {}
        for id_, words in list_alpha:
            if str(words[0]) not in sub_groups.keys():
                sub_groups[str(words[0])] = [(id_, words)]
            else:
                sub_groups[str(words[0])].append((id_, words))

        keys = sorted([i for i in sub_groups.keys()])
        list_alpha = []
        for key in keys:
            sub_groups[key].sort(key=lambda x: x[0])
            list_alpha += sub_groups[key]

        sub_groups = {}
        for id_, words in list_numeric:
            if str(words[0]) not in sub_groups.keys():
                sub_groups[str(words[0])] = [(id_, words)]
            else:
                sub_groups[str(words[0])].append((id_, words))

        keys = sorted([i for i in sub_groups.keys()])
        list_numeric = []
        for key in keys:
            sub_groups[key].sort(key=lambda x: x[0])
            list_numeric += sub_groups[key]

        return list_numeric + list_numeric


if __name__ == '__main__':
    s = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    solution = Solution()
    answer = solution.reorderLogFiles(s)
    print(answer)
