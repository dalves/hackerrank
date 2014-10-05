# Problem statement is here:
# https://www.hackerrank.com/contests/back2school14/challenges/fibonacci-modified/

a, b, n = map(int, raw_input().strip().split())

series = [0, a, b]

while len(series) <= n:
    series.append(series[-1]**2 + series[-2])

print series[n]
