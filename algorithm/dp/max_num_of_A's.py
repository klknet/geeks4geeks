"""
How to print maximum number of A's using given four keys.
Imagine you have a special keyboard with following keys:
Key 1: Prints 'A' on screen.
Key 2: Ctrl-A: Select screen.
Key 3: Ctrl-C: Copy selection to buffer.
Key 4: Ctrl-V: Print buffer on screen appending it after what has already been printed.
If you can only press the keyboard for N times (with above four keys), write a program to produce maximum number of A's

Below are few important points to note.
a)For N<7, the output is N itself.
b)Ctrl V can be used multiple times to print current buffer. The idea is to compute the optimal string length for N
keystrokes by using a simple insight. The sequence of N keystrokes which produces a optimal string length will end with
a suffix of Ctrl-A, Ctrl-C followed by only Ctrl-V's. (For N>6).

The task is to find the break=point after which we get above suffix of keystrokes. Definition of breakpoint is that instance
after which we need to only press Ctrl-A, Ctrl-C once and the only Ctrl-V's afterwards to generate the optimal length. If
we loop from N-3 to 1 and choose each of these values for the break-point, and compute that optimal string they would
produce. Once the loops end, we will have the maximum of the optimal lengths for various break-points, thereby giving us
the optimal length for N keystrokes.
"""


def max_num_of_A(n):
    if n < 7:
        return n
    max_num = 0
    for i in range(n - 3, 0, -1):
        num = (n - i - 1) * max_num_of_A(i)
        max_num = max(num, max_num)
    return max_num


def max_num_dp(n):
    if n < 7:
        return n
    dp = [0] * (n+1)
    for i in range(7):
        dp[i] = i
    for k in range(7, n+1):
        max_num = 0
        for i in range(k-3, 0, -1):
            curr = (k - i - 1) * dp[i]
            max_num = max(max_num, curr)
        dp[k] = max_num
    return dp[n]


for i in range(1, 21):
    print('Maximum number of A with', i, 'keystrokes is', max_num_of_A(i))
    print('DP-Maximum number of A with', i, 'keystrokes is', max_num_dp(i))
