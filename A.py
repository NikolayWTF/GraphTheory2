n = int(input("Введите количество вершин "))
i = 0
A = []
while i < n:

    B = [0] * n
    A.append(B)
    i += 1

i = 0
while i < n:
    print(f"Введите список смежности для {i+1} вершины")
    a = list(map(int, input().split()))
    l = len(a)
    j = 0
    while j < l:
        A[i][a[j]-1] += 1
        j += 1

    i += 1

i = 0
while i < n:
    print(A[i])
    i += 1

#5
#2 5
#1 3 5
#2 4 5
#3
#1 2 3