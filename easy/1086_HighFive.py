class Solution:

    def highFive(self, items: list) -> list:
        '''
        Time Complexity = (N)
        Space Complexity = (N)
        '''
        dict_ = dict()
        keys_ = []
        for id_, score in items:
            if id_ not in dict_.keys():
                dict_[id_] = [score]
                keys_.append(id_)
            else:
                dict_[id_].append(score)

        keys_.sort()
        list_ = []
        for id_ in keys_:
            dict_[id_].sort()
            average = int(sum(dict_[id_][-5:]) / 5)
            list_.append([id_, average])

        return list_


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60],
             [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]

    solution = Solution()
    answer = solution.highFive(items)
    print(answer)
