# SOLVED?

# 2020 A
# Tambourine has prepared a fitness program so that she can become more fit!
# The program is made of N sessions. During the i-th session, Tambourine will
# exercise for Mi minutes. The number of minutes she exercises in each session
# are strictly increasing.

# The difficulty of her fitness program is equal to the maximum difference
# in the number of minutes between any two consecutive training sessions.

# To make her program less difficult, Tambourine has decided to add up to K
# additional training sessions to her fitness program. She can add these
# sessions anywhere in her fitness program, and exercise any positive integer
# number of minutes in each of them. After the additional training session are
# added, the number of minutes she exercises in each session must still be
# strictly increasing. What is the minimum difficulty possible?

tests = int(input())
for t in range(1, tests + 1):
    n, k = [int(d) for d in input().split(" ")]
    sessions = [int(s) for s in input().split(" ")]
    diffs = [0] * (n-1)
    for i in range(1, n):
        diffs[i-1] = sessions[i] - sessions[i-1]

    i = 1
    j = 10**9
    while(i < j):
        d_optimal = (i + j) // 2
        k_sum = 0
        for d in diffs:
            k_sum += (d - 1) // d_optimal
        if k_sum > k:
            i = d_optimal + 1
        else:
            j = d_optimal

    print(f"case #{t}: {i}")
