# Problem statement:
# https://www.hackerrank.com/contests/back2school14/challenges/almost-sorted
import sys

n = int(raw_input())
d = map(int, raw_input().split())

def is_sorted(seq):
    for i in xrange(1, len(seq)):
        if seq[i-1] > seq[i]:
            return False
    return True

if is_sorted(d):
    print 'yes'
    sys.exit()
else:
    less_indices = []
    for i in xrange(1, n):
        if d[i] < d[i-1]:
            less_indices.append(i)
    if len(less_indices) == 1:
        i, j = less_indices[0]-1, less_indices[0]
        d[i], d[j] = d[j], d[i]
        if is_sorted(d):
            print 'yes'
            print 'swap', less_indices[0], less_indices[0]+1
            sys.exit()
    elif len(less_indices) == 2:
        for i in [less_indices[0]-1, less_indices[0]]:
            for j in [less_indices[1]-1, less_indices[1]]:
                if i != j:
                    d[i], d[j] = d[j], d[i]
                    if is_sorted(d):
                        print 'yes'
                        a, b = sorted([i+1, j+1])
                        print 'swap', a, b
                        sys.exit()
                    else:
                        # Restore original list
                        d[i], d[j] = d[j], d[i]


    elif less_indices[-1] - less_indices[0] == len(less_indices) - 1:
        # reverse
        l, r = less_indices[0]-1, less_indices[-1]+1
        d[l:r] = reversed(d[l:r])
        if is_sorted(d):
            print 'yes'
            print 'reverse', l+1, r
            sys.exit()
print 'no'
