"""
You are given a set of n types of 3-D rectangular boxes, where the ith box has height h(i), width w(i), depth d(i)(all
real numbers). You want to create a stack of boxes which is as tall as possible, but you can only stack a box on top of
another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of
higher box. Of course, you can rotate a box so that any side functions as its base. It is also allowable to use multiple
instances of the same type of box.
Following is the solution based on DP solution of LIS problem.
1)Generate all 3 rotations of all boxes. The size of rotation array becomes 3 times the size of original array. For simplicity
we consider depth as always smaller than or equal than width.
2)Sort the above generated array in decreasing order of base area
3)After sorting the boxes, the problem is same as LIS problem with follow optimal substructure property.
MSH(i) = Maximum possible stack height with box i at top of stack
MSH(i) = max(MSH(j) + height(i) where j<i and w(j)>w(i) and d(j)>d(j)
if there is no such j then MSH(i) = height(i)
4)To get overall maximum height, we return max(MSH(i)) where 0<i<n
"""


def msh(arr):
    n = len(arr)
    rotation = []
    # generate the 3n rotation array.
    for i in range(n):
        rotation.append(Box(arr[i].d, min(arr[i].w, arr[i].h), max(arr[i].w, arr[i].h), arr[i].w * arr[i].h))
        rotation.append(Box(arr[i].w, min(arr[i].d, arr[i].h), max(arr[i].d, arr[i].h), arr[i].d * arr[i].h))
        rotation.append(Box(arr[i].h, min(arr[i].d, arr[i].w), max(arr[i].d, arr[i].w), arr[i].d * arr[i].w))
    rotation.sort(reverse=True)
    # t[i] stores the maximum stack height with ith box at the top of the stack.
    n = 3 * n
    t = [0] * n
    # initial the table
    for i in range(n):
        t[i] = rotation[i].h
    for i in range(1, n):
        for j in range(i):
            if rotation[j].w > rotation[i].w and rotation[j].d > rotation[i].d and t[i] < t[j] + rotation[i].h:
                t[i] = t[j] + rotation[i].h
    return max(t)


class Box:
    def __init__(self, h, d, w, area=0):
        self.h = h
        self.d = d
        self.w = w
        self.area = area

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area


arr = [Box(4, 6, 7), Box(1, 2, 3), Box(4, 5, 6), Box(10, 12, 32)]
print(msh(arr))
