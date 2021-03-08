# SOLVED? NO
# N stacks, K plates per stack, take P plates
# DP - memoize?

t = int(input())
for t in range(1, t+1):
    n, k, p = [int(d) for d in input().split(" ")]
    stacks = []
    for _ in range(n):
        stack = [int(d) for d in input().split(" ")]
        stacks.append(stack)
    sum = [[0 for j in range(k+1)] for i in range(n)]
    for i in range(n):
        for j in range(1, k+1):
            sum[i][j] = sum[i][j - 1] + stacks[i][j-1]

    dp = [[0 for j in range(p+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(p+1):
            for x in range(min(j, k)+1):
                dp[i][j] = max(dp[i][j], sum[i-1][x] + dp[i-1][j-x])

    print(f"case #{t}: {dp[n][p]}")
