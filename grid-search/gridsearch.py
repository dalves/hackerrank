# Problem statement is here:
# https://www.hackerrank.com/contests/back2school14/challenges/the-grid-search

def ints():
    return map(int, raw_input().split())

T = ints()[0]
for i in xrange(T):
    R, C = ints()

    grid = []
    for i in xrange(R):
        grid.append(raw_input())

    r, c = ints()
    pattern = []
    for i in xrange(r):
        pattern.append(raw_input())

    found = False
    for r_off in xrange(0, R-r+1):
        if found:
            break
        for c_off in xrange(0, C-c+1):
            for row in xrange(r):
                if grid[r_off+row][c_off:c_off+c] != pattern[row]:
                    break
            else:
                found = True
                break
    print 'YES' if found else 'NO'
