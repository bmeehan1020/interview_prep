# SOLVED?

# CTCI 8.1
def triple_step(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n-1]


assert triple_step(1) == 1
assert triple_step(4) == 7
print(triple_step(100))
