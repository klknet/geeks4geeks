"""
Print International gender symbol for females.
"""
import math


def print_symbol(n):
    # Outer loop for height
    for i in range(2 * n + 1):
        # Inner loop for width
        for j in range(2 * n + 1):
            dist = math.sqrt((i - n) ** 2 + (j - n) ** 2)
            if n - 0.5 < dist < n + 0.5:
                print('$', end='')
            else:
                print(' ', end='')
        if i == n:
            print(' happy womens day', end='')
        print('')
    for i in range(n + 1):
        if i == n // 2+1:
            for j in range(2*n+1):
                if n - n // 2 <= j < n + n // 2 + 1:
                    print('$', end='')
                else:
                    print(' ', end='')
        else:
            for j in range(n + 1):
                if j == n:
                    print('$', end='')
                else:
                    print(' ', end='')
        print('')


print_symbol(5)
