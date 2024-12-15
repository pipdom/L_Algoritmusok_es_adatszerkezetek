def nearest_smaller_values(arr):
    stack = []  # Verem a pozíciók tárolására
    result = []  # Kimeneti lista
    
    for i in range(len(arr)):
        # Stackből eltávolítjuk azokat, amelyek nagyobbak vagy egyenlők az aktuális elemnél
        while stack and arr[stack[-1] - 1] >= arr[i]:
            stack.pop()
        
        # Ha a stack nem üres, a tetején lévő index lesz a válasz
        if stack:
            result.append(stack[-1])
        else:
            result.append(0)  # Ha nincs kisebb érték, 0 a válasz
        
        # Az aktuális pozíciót (1-alapú index) hozzáadjuk a stackhez
        stack.append(i + 1)
    
    return result

# Bemenet beolvasása
n = int(input())
arr = list(map(int, input().split()))
result = nearest_smaller_values(arr)

# Kimenet kiírása
print(" ".join(map(str, result)))
