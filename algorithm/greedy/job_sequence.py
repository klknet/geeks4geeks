"""
Q: given a arr of jobs which have deadline time and can earn profit if finish the job before the deadline, it is also that
each job can process on an unit time, at every time ,only ont job can be processed, find the maximum profit.

1)Sort the job arr according decreasing order
2)Process the job for each:
 a)put the job to result sequence if the job fit the deadline
"""


def print_job_scheduling(arr, t):
    n = len(arr)
    # sort accord decreasing order
    arr.sort(key=lambda x: x[2], reverse=True)
    # time slots for indicate job fit the deadline
    slots = [False] * t
    job = [-1] * t
    for i in range(n):
        for j in range(arr[i][1] - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                job[j] = arr[i][0]
                break

    print(job)


arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
arr = [['a', 4, 20],
       ['b', 1, 10],
       ['c', 1, 40],
       ['d', 1, 30]]
print_job_scheduling(arr, 4)