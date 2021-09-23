def valid(mas, n):
    i = 0
    v = 1
    while i < n and v:
        j = i+1
        while j < n:

            if mas[i][j] != mas[j][i]:
                v = 0
            j += 1
        i += 1
    return v

n = int(input("Введите количество вершин "))
i = 0
A = []
B = []
while i < n:
    print(f"Введите {i+1} строку матрицы смежности")
    b = list(map(int, input().split()))
    A.append(b)
    i += 1

valid = valid(A, n)
if valid:

    i = 0
    while i < n:
        j = 0
        B.append([])
        while j < n:
            if A[i][j] == 1:
                B[i].append(j + 1)

            j += 1
        i += 1
    i = 0

    while i < n:
        ans = ""
        for _ in B[i]:
            ans += str(_) + " "
        print(f"{i+1}: " +  '{ '  + ans + '}' )
        i += 1
else:
    print("Вы ввели не матрицу смежности. ")
            
#5
# 0 1 0 0 1
# 1 0 1 0 1
# 0 1 0 1 1
# 0 0 1 0 0
# 1 1 1 0 0