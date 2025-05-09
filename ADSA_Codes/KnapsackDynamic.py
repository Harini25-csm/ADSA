def merge_purge(S1, S2):
    merged = sorted(S1 + S2, key=lambda x: (x[1], -x[0]))
    result = []
    max_profit = -1
    for profit, weight in merged:
        if profit > max_profit:
            result.append((profit, weight))
            max_profit = profit
    return result

def trace_back(S, p, w, m, n, x):
    for i in range(n - 1, 0, -1):
        (PX, WX) = S[i][-1]
        Wp = -1
        best_pair = None
        for (P, W) in S[i - 1]:
            if W + w[i] <= m and W > Wp:
                Wp = W
                best_pair = (P + p[i], W + w[i])
        x[i] = 0 if PX > (best_pair[0] if best_pair else 0) else 1
        m -= w[i] if x[i] == 1 else 0
    x[0] = 0 if (0, 0) in S[0] else 1

def DKP(p, w, n, m):
    S = [[] for _ in range(n)]
    S[0] = [(0, 0)]

    for i in range(1, n):
        S1 = [(P + p[i], W + w[i]) for (P, W) in S[i - 1] if W + w[i] <= m]
        S[i] = merge_purge(S[i - 1], S1)

    (PX, WX) = S[n - 1][-1]
    Wp = -1
    best_pair = None
    for (P, W) in S[n - 2]:
        if W + w[n - 1] <= m and W > Wp:
            Wp = W
            best_pair = (P + p[n - 1], W + w[n - 1])

    x = [0] * n
    x[-1] = 0 if PX > (best_pair[0] if best_pair else 0) else 1
    trace_back(S, p, w, m, n, x)

    solution_profit = sum(p[i] for i in range(n) if x[i] == 1)
    print("Solution vector (x):", x)
    print("Maximum profit:", solution_profit)

# --- Main ---
n = int(input("Enter number of items: "))
p = list(map(int, input("Enter profits of items separated by space: ").split()))
w = list(map(int, input("Enter weights of items separated by space: ").split()))
m = int(input("Enter maximum capacity of knapsack: "))

if len(p) != n or len(w) != n:
    print("Error: profits and weights must have exactly n elements.")
else:
    DKP(p, w, n, m)
