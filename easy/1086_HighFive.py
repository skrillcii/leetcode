import collections
import heapq


class Solution:

    def highFive_self_trial(self, items: list) -> list:
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

    def highFive_sort(self, items: list) -> list:
        '''
        Time Complexity = (N)
        Space Complexity = (N)
        '''
        items.sort(reverse=True)
        id_ = items[0][0]
        curr = []
        list_ = []

        for i, score in items:
            if i == id_:
                if len(curr) < 5:
                    curr.append(score)
            else:
                list_.insert(0, [id_, sum(curr) // 5])
                id_ = i
                curr = [score]
        list_.insert(0, [id_, sum(curr) // 5])
        return list_

    def highFive_priority_queue(self, items: list) -> list:
        '''
        Time Complexity = (N)
        Space Complexity = (N)
        '''
        students = collections.defaultdict(list)
        results = []

        for student, score in items:
            heapq.heappush(students[student], -score)

        for student in students:
            avg_scores = sum(-heapq.heappop(students[student])
                             for i in range(0, 5)) // 5
            results.insert(0, [student, avg_scores])
        return results


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60],
             [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    items = [[1, 100], [7, 100], [1, 100], [7, 100], [1, 100],
             [7, 100], [1, 100], [7, 100], [1, 100], [7, 100]]

    solution = Solution()
    answer = solution.highFive_self_trial(items)
    print(answer)
    answer = solution.highFive_sort(items)
    print(answer)
    answer = solution.highFive_priority_queue(items)
    print(answer)
