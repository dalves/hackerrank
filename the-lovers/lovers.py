# Problem statement:
# https://www.hackerrank.com/contests/back2school14/challenges/the-lovers

from __future__ import division

def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def lucas(n, k, p):
    result = 1
    while n:
        result *= choose(n % p, k % p)
        result = result % p
        n //= p
        k //= p
    return result


def solve(n, k):
    return lucas(n - k + 1, k, 100003)


T = int(raw_input())
for i in xrange(T):
    n, k = map(int, raw_input().split())
    print solve(n, k)
