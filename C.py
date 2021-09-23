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
A = [] # Матрица смежности
D = [] #Матрица степеней
L = [] #Матрица Лапласа
I = [] #Матрица инцидентности
C = []
r = 0
while i < n:
    print(f"Введите {i + 1} строку матрицы смежности")
    b = list(map(int, input().split()))
    c = b.count(1) # Сразу читаем степень этой строки
    r += c # Считаем удвоенное количество рёбер
    C.append(c) # Запоминаем степень i-й вершины
    D.append([0]*n)
    A.append(b)
    i += 1

valid = valid(A, n) # Проверяем корректность входных данных

if valid:
    r //= 2 # Считаем количество рёбер
    i = 0
    while i < n:# Делаем матрицу инцидентности размером rxn
        I.append([0]*r)
        i += 1


    i = 0
    j = 0
    ind = 0
    while i < n: # Заполняем матрицу инцидентности

        j = i
        while j < n:
            if A[i][j] == 1:
                I[i][ind] = 1
                I[j][ind] = 1
                ind += 1
            j += 1
        i += 1

    i = 0
    j = 0
    while i < n: # Заполняем матрицу степеней и матрицу Лапласа

        j = 0
        L.append([0]*n)
        while j < n:

            if i == j:
                D[i][j] = C[i]
            L[i][j] = D[i][j] - A[i][j] # Матрица Лапласа = (матрица степеней - матрица смежности)

            j += 1
        i += 1


    i = 0
    print("Матрица инцидентности")
    while i < n: # Вывод матрицы инцидентности
        print(I[i])
        i += 1
    print ()

    i = 0

    print("Матрица степеней")
    while i < n: # Вывод матрицы степеней
        print(D[i])
        i += 1

    i = 0
    print()
    print("Матрица Лапласа")
    while i < n:
        print(L[i])
        i += 1

else:
    print("Вы ввели не матрицу смежности. ")
