MOD = 10**9 + 7

# Következő oszlop maszkjainak generálása
def generate_next_mask(n, curr_mask, new_mask, j, next_mask):
    if j == n:  # Ha elértük az oszlop végét
        next_mask.append(new_mask)
        return
    
    # 2x1-es csempe elhelyezése
    if j + 1 < n and ((1 << j) & curr_mask) == 0 and ((1 << (j + 1)) & curr_mask) == 0:
        generate_next_mask(n, curr_mask, new_mask, j + 2, next_mask)
    
    # 1x2-es csempe elhelyezése
    if (1 << j) & curr_mask == 0:
        generate_next_mask(n, curr_mask, new_mask + (1 << j), j + 1, next_mask)
    
    # Lépés a következő cellára
    if (1 << j) & curr_mask != 0:
        generate_next_mask(n, curr_mask, new_mask, j + 1, next_mask)

# Rekurzív függvény a rács kitöltésére
def count_ways(n, m, i, mask, dp):
    if i == m:  # Ha elértük az utolsó oszlopot
        return 1 if mask == 0 else 0
    
    if dp[i][mask] != -1:  # Memoizált érték visszaadása
        return dp[i][mask]
    
    next_mask = []  # Következő oszlop maszkjainak generálása
    generate_next_mask(n, mask, 0, 0, next_mask)
    
    ans = 0
    for x in next_mask:  # Rekurzív hívás minden lehetséges maszkra
        ans = (ans + count_ways(n, m, i + 1, x, dp)) % MOD
    
    dp[i][mask] = ans  # Memoizálás
    return ans

# Feladat megoldása
n, m = map(int, input().split())  # Bemenet beolvasása
dp = [[-1] * (1 << n) for _ in range(m)]  # DP tömb inicializálása
result = count_ways(n, m, 0, 0, dp)  # Megoldás kiszámítása
print(result)  # Eredmény kiírása
