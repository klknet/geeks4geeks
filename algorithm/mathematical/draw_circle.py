"""
Draw a circle without floating point arithmetic.
"""


def draw_circle(r):
    n = 2 * r + 1
    for i in range(n):
        for j in range(n):
            x = i-r
            y = j-r
            if x*x + y*y <= r*r+1:
                print('.', end='')
            else:
                print(' ', end='')
        print()


draw_circle(8)