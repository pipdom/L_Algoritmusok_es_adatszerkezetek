import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
input = sys.stdin.read

def mark_dfs(node, vis, adj):
    vis[node] = True
    for child in adj[node]:
        if not vis[child]:
            mark_dfs(child, vis, adj)

def dfs(node, dp, adj, n, child):
    if node == n:  # Alapeset: az \( n \)-edik városba értünk
        dp[node] = 1
        return 1
    if dp[node] != -1:  # Memoizáció
        return dp[node]

    max_len = 0
    for v in adj[node]:
        tmp = dfs(v, dp, adj, n, child)
        if tmp > 0 and 1 + tmp > max_len:  # Csak akkor számoljuk, ha az \( n \)-edik csúcsból érkezünk
            child[node] = v
            max_len = 1 + tmp

    dp[node] = max_len
    return dp[node]

# Bemenet feldolgozása
data = input().split()
idx = 0
n = int(data[idx])
m = int(data[idx + 1])
idx += 2

adj = defaultdict(list)
for _ in range(m):
    x = int(data[idx])
    y = int(data[idx + 1])
    idx += 2
    adj[x].append(y)

# Ellenőrizzük, hogy az n város elérhető-e az 1-es városból
vis = [False] * (n + 1)
mark_dfs(1, vis, adj)
if not vis[n]:
    print("IMPOSSIBLE")
else:
    dp = [-1] * (n + 1)  # Dinamikus programozási tömb
    child = [0] * (n + 1)  # Utakat követő tömb

    # Hosszú út kiszámítása
    dfs(1, dp, adj, n, child)

    # Útvonal rekonstruálása
    path = []
    node = 1
    while node:
        path.append(node)
        node = child[node]

    print(len(path))
    print(" ".join(map(str, path)))
