import sys
from urllib import request, response
import re


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


# * 表示以元祖传入
def test_fun(a, b, *args):
    print(a + b, args)


# ** 表示已字典传入
def test_fun1(a, b, **kwargs):
    print(a + b, kwargs)


def test_rest():
    URL = "https://dev.xylink.com/console/api/rest/v1/en/mobile/balance?securityKey=9d3631d5257c524163b841c339a8e79316f30b1d6ad&enterpriseId=ff8080815e0a0cd8015e0dc295a8002c"
    # URL = "https://dev.xylink.com/console/api/rest/v1/en/mobile/recordPage?page=0&size=10&startTime=1572537600000&securityKey=9d3631d5257c524163b841c339a8e79316f30b1d6ad&enterpriseId=ff80808154b854a20154b855605c0000&endTime=1577721600000";
    req = request.Request(URL)
    res = request.urlopen(req)
    if res.status == 200:
        print(type(res))
        print(res.info(), end='')
        print(res.read().decode("utf8"))


def test_re():
    s = 'AB23G4HDF567'
    matched = re.match('AB(\d+)', s)
    if matched:
        print(matched.group(1))
    matched = re.search('\d+', s)
    if matched:
        print(matched.group(0))


if __name__ == '__main__':
    # test_iter([1, 2, 3, 4])
    # test_yield(10)
    # print()
    # print(sys.path)
    # print(sys.argv)
    # test_fun(2, 5, 6, 8)
    # test_fun1(3, 4, c=7, d=9)
    # test_rest()
    test_re()
