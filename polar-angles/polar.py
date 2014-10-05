# Problem statement here:
# https://www.hackerrank.com/contests/back2school14/challenges/polar-angles
import math

n = int(raw_input())
points = []
while n > 0:
    n -= 1
    x, y = map(int, raw_input().split())
    points.append((x,y))

result = [((math.atan2(y, x) + 2 * math.pi) % (2*math.pi), (x**2 + y**2), (x,y)) for x, y in points]
result.sort()

for point in result:
    x,y = point[2]
    print x, y
