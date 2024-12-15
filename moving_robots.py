N = 8  # Sakktábla mérete: 8x8
SZ = N * N  # Összes mező száma (64)
maxK = 101  # Maximális lépésszám

K = int(input())  # Bemenet: lépések száma
expected = 0.0  # Várható üres mezők száma
ans = [1.0] * SZ  # Minden mező kezdeti valószínűsége 1.0 (robot van rajta)
dp = [[0.0] * SZ for _ in range(maxK)]  # Dinamikus programozási tömb (dp)

# Iteráció minden mező kezdőpozíciójára
for start in range(SZ):
    # dp alaphelyzetbe állítása az aktuális kezdőpozícióhoz
    for i in range(maxK):
        for j in range(SZ):
            dp[i][j] = 0.0

    dp[0][start] = 1.0  # Kezdetben a robot 100% valószínűséggel a start mezőn van

    # Lépések szimulációja
    for k in range(K):
        for u in range(SZ):
            V = []  # Szomszédos mezők listája
            # Fel (csak ha nem az első sorban vagyunk)
            if N <= u:
                V.append(u - N)
            # Le (csak ha nem az utolsó sorban vagyunk)
            if u < N * (N - 1):
                V.append(u + N)
            # Balra (csak ha nem az első oszlopban vagyunk)
            if u % N != 0:
                V.append(u - 1)
            # Jobbra (csak ha nem az utolsó oszlopban vagyunk)
            if u % N != N - 1:
                V.append(u + 1)

            # Szomszédos mezőkre terjesztjük a valószínűséget
            for v in V:
                dp[k + 1][v] += dp[k][u] / len(V)

    # Minden mező valószínűségét frissítjük
    for u in range(SZ):
        ans[u] *= (1 - dp[K][u])  # 1 - dp[K][u]: valószínűség, hogy üres

# Az összes mező üres valószínűségének összegzése
for i in range(SZ):
    expected += ans[i]

# Kimenet 6 tizedesjegyre kerekítve
print(f"{expected:.6f}")
