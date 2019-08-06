"""
Program for tower of hanoi.
The pattern here is:
Shift n-1 dists from A to B.
Shift last dist from A to C.
Shift n-1 dists from B to C.
"""


def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print('Move dist', 1, from_rod, '-->', to_rod)
    else:
        tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
        print('Move dist', n, from_rod, '-->', to_rod)
        tower_of_hanoi(n-1, aux_rod, from_rod, to_rod)


tower_of_hanoi(4, 'A', 'C', 'B')
