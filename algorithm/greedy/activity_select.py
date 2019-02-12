# You are given n activities with their start and finish time, Select the maximum number of activities that can be
#  performed by a single person, assuming that a person can only work on a single activity at a time


def select_activity(start, end):
    n = len(start)
    i = 0
    res = [i]
    for j in range(n):
        if end[i] <= start[j]:
            i = j
            res.append(i)
    return res


def select_unsort_activity(activities):
    activities.sort(key=lambda act: act[1])
    n = len(activities)
    i = 0
    res = [i]
    for j in range(n):
        if activities[j][0] >= activities[i][1]:
            i = j
            res.append(i)
    return res


if __name__ == '__main__':
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    print(select_activity(start, end))
    print(select_unsort_activity([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
