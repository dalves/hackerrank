# N = victims
# K = hitmen
N, K = map(int, raw_input().split())
cost = []

MASK = 2<<K
INF = 10**8-1

# cost[hitman][victim]
for i in xrange(K):
    prices = map(int, raw_input().split())
    prices.reverse()
    cost.append(prices)


# dp[used_hitman_mask][num_dead] = total_cost
dp = []
for i in xrange(MASK):
    dp.append([INF] * (N + 1))

dp[0][0] = 0

def hitman_available(hitman, mask):
    return not (2 << hitman) & mask

def use_hitman(hitman, mask):
    return mask | (2 << hitman)

for already_killed in xrange(0, N):
    for mask in xrange(0, MASK):
        for hitman in xrange(0, K):
            if hitman_available(hitman, mask):
                mask_after = use_hitman(hitman, mask)
                for num_to_kill in xrange(1, N - already_killed+1):
                    dp[mask_after][num_to_kill + already_killed] = min(
                        dp[mask_after][num_to_kill + already_killed],
                        dp[mask][already_killed] + sum(cost[hitman][already_killed:already_killed+num_to_kill]))

print min(dp[i][N] for i in xrange(MASK))
