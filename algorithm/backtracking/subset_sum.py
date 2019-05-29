"""
Subset sum problem.
"""

total_nodes = 0


def subset_sum(s, target_num):
    s_size = len(s)
    t = [0] * s_size
    subset_util(s, t, s_size, 0, 0, 0, target_num)


def subset_util(s, t, s_size, t_size, cur_sum, ite, target_num):
    global total_nodes
    total_nodes += 1
    if cur_sum == target_num:
        print_subset(t, t_size)
        if ite < s_size:
            subset_util(s, t, s_size, t_size - 1, cur_sum - s[ite], ite + 1, target_num)
    else:
        for i in range(ite, s_size, 1):
            t[t_size] = s[i]
            subset_util(s, t, s_size, t_size + 1, cur_sum + s[i], i + 1, target_num)


def print_subset(t, t_size):
    for i in range(t_size):
        print(t[i], end=' ')
    print('')


s = [10, 7, 5, 18, 12, 20, 15]
subset_sum(s, 35)
print(total_nodes)
