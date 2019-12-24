import sys


def test_iter(arr):
    it = iter(arr)
    while True:
        try:
            print(next(it), end=' ')
        except StopIteration:
            return


def test_yield(n):
    itr = _generate(n)
    while True:
        try:
            print(next(itr), end=' ')
        except StopIteration:
            return


def _generate(n):
    a = 0
    while a < n:
        yield a
        a += 1


if __name__ == '__main__':
    test_iter([1, 2, 3, 4])
    test_yield(10)
    print()
    print(sys.path)
    print(sys.argv)
