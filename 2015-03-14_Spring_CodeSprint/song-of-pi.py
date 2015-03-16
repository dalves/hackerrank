import re

pi = '31415926535897932384626433833'
cases = int(raw_input())

for i in xrange(cases):
    digits = ''.join(str(len(x)) for x in re.findall('[A-Za-z]+', raw_input()))
    print "It's a pi song." if pi.startswith(digits) else "It's not a pi song."
