def sum_digits(n):
    return sum(int(x) for x in str(n))

def prime_factors(n):
    factors = []
    for i in xrange(2, n):
        if i*i > n:
            break
        elif n % i == 0:
            while n % i == 0:
                factors.append(i)
                n /= i
    if n > 1:
        factors.append(n)
    return factors

n = int(raw_input())

factors = prime_factors(n)
print '1' if len(factors) > 1 and sum_digits(n) == sum(sum_digits(x) for x in factors) else '0'
