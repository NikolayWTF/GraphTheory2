from tkinter import *
import math
v = 1
ans = 1

def Visualisation(n, m, array):
    k = n*m

    root = Tk()
    c = Canvas(root, width="2048", heigh="1024")  # Создаю окно
    c.pack()
    centerX = 700.0
    centerY = 350.0
    radius = 10 * k
    angel = 2 * math.pi / k
    X = []
    Y = []
    i = 0
    ind1 = 1
    ind2 = 1
    while i < k:
        x = centerX + radius * math.sin(i * angel)  # Координата новой вершины по x
        y = centerY + radius * math.cos(i * angel)  # И по y
        X.append(x)
        Y.append(y)
        c.create_oval(x, y, x + 10, y + 10, fill="black")  # Рисуем вершину

        if ind2 > m:
            ind1 += 1
            ind2 = 1
        if (i < k / 4):
            c.create_text(x + 20, y + 20, text="{" + str(ind2) + ", " + str(ind1) + "}")
        elif (i < k / 2):
            c.create_text(x + 30, y + 2, text="{" + str(ind2) + ", " + str(ind1) + "}")
        elif (i < 3 * k / 4):
            c.create_text(x - 15, y - 9, text="{" + str(ind2) + ", " + str(ind1) + "}")
        else:
            c.create_text(x - 20, y + 10, text="{" + str(ind2) + ", " + str(ind1) + "}")
        ind2 += 1
        i += 1

    i = 0
    while i < k:
        l = len(array[i])  # Узнаём степень i-й вершины
        j = 0
        while j < l:
            c.create_line(X[i] + 5, Y[i] + 5, X[array[i][j] - 1] + 5, Y[array[i][j] - 1] + 5)
            j += 1
        i += 1
    root.mainloop()


def Decart(n, m, C):
    k = n * m
    i = 0
    while i < k:
        C.append([])
        i += 1
    ind = 0
    while ind < k:
        i = 0
        while i < m:
            j = 0
            l = len(B[i])
            while j < l:
                C[ind + i].append(B[i][j] + ind)
                j += 1
            i += 1
        ind += m


    i = 0
    while i < m:
        ind = 0
        indA = 0
        while ind < k:
            j = 0
            l = len(A[indA])
            while j < l:
                C[ind + i].append((A[indA][j] - 1) * m + i + 1)
                j += 1
            ind += m
            indA += 1
        i += 1

def Tenzor(n, m, T):
    k = n * m
    i = 0
    while i < k:
        T.append([])
        i += 1

    ind = 0
    while ind < k:
        ind1 = math.floor(ind / m)
        ind2 = ind - ind1 * m
        tempA = []
        tempB = []

        j = 0
        l1 = len(A[ind1])
        while j < l1:
            tempA.append(A[ind1][j])
            j += 1
        j = 0
        l2 = len(B[ind2])
        while j < l2:
            tempB.append(B[ind2][j])
            j += 1
        l1 = len(tempA)
        l2 = len(tempB)
        i = 0
        while i < l1:
            j = 0
            while j < l2:
                T[ind].append((tempA[i] - 1) * m + tempB[j])
                j += 1
            i += 1
        ind += 1

def Leksika(n, m, L):

    k = n * m
    i = 0
    while i < k:
        L.append([])
        i += 1
    i = 0
    while i < n:
        j = 0
        l = len(A[i])
        while j < l:
            ind = i * m
            while ind < ((i + 1) * m):
                t = 1
                while t <= m:
                    L[ind].append((A[i][j] - 1) * m + t)
                    t += 1
                ind += 1
            j += 1
        i += 1
    i = 0
    ind = 0
    while i + ind < k:
        if (i < m):
            j = 0
            l = len(B[i])
            while j < l:
                L[i + ind].append(B[i][j] + ind)
                j += 1
            i += 1
        else:
            i = 0
            ind += m

def Diz(n, m, D):

    k = n * m
    i = 0
    while i < k:
        D.append([])
        i += 1
    i = 0
    while i < n:
        j = 0
        l = len(A[i])
        while j < l:
            ind = i * m
            while ind < ((i + 1) * m):
                t = 1
                while t <= m:
                    D[ind].append((A[i][j] - 1) * m + t)
                    t += 1
                ind += 1
            j += 1
        i += 1

    i = 0
    while i < m:
        j = 0
        l = len(B[i])
        while j < l:
            ind = 0
            while ind <= ((n - 1) * m):
                t = 0
                while t <= ((n - 1) * m):
                    D[i + ind].append(B[i][j] + t)
                    t += m
                ind += m
            j += 1
        i += 1

def Root(n, m, K):
    k = n * m
    i = 0
    while i < k:
        K.append([])
        i += 1
    i = 0
    while i < m:
        l = len(B[i])
        j = 0
        while j < l:
            K[i].append(B[i][j])
            j += 1
        i += 1
    ind = 0
    while ind < m:
        i = 0
        while i < n:
            l = len(A[i])
            j = 0
            while j < l:
                K[i * m + ind].append((A[i][j] - 1) * m + 1 + ind)
                j += 1
            i += 1
        ind += 1

while v == 1:

    if ans == 1:
        n = int(input("Введите количество вершин первого графа"))
        m = int(input("Введите количество вершин второго графа"))
        AA = []
        BB = []
        i = 0
        while i < n:
            a = list(map(int, input(f"Введите {i+1} строку матрицы смежности вершин первого графа").split()))
            AA.append(a)
            i += 1
        i = 0
        while i < m:
            a = list(map(int, input(f"Введите {i + 1} строку матрицы смежности вершин второго графа").split()))
            BB.append(a)
            i += 1

        i = 0
        A = []
        B = []
        while i < n:
            j = 0
            A.append([])
            while j < n:
                if AA[i][j] == 1:
                    A[i].append(j + 1)

                j += 1
            i += 1

        i = 0
        while i < m:
            j = 0
            B.append([])
            while j < m:
                if BB[i][j] == 1:
                    B[i].append(j + 1)

                j += 1
            i += 1

        print("Выберете цифру, чтобы сделать соответствующее действие")
        #print("1 Ввести новые данные")
        print("2 Вывести Декартово произведение с уже введёнными данными")
        print("3 Вывести Тензерное произведение с уже введёнными данными")
        print("4 Вывести Сильное произведение с уже введёнными данными")
        print("5 Вывести Лексикографическое произведение с уже введёнными данными")
        print("6 Вывести Дизъюнктивное произведение с уже введёнными данными")
        #print("5 Вывести Лексикографическое произведение с уже введёнными данными")

        #print("6 Выйти из программы ")
        ans = int(input())

    elif ans == 2:
        C = []
        Decart(n, m, C)
        Visualisation(n, m, C)

        print("Выберете цифру, чтобы сделать соответствующее действие")
        print("1 Ввести новые данные")
        print("2 Вывести Декартово произведение с уже введёнными данными")
        print("3 Вывести Тензерное произведение с уже введёнными данными")
        print("4 Вывести Сильное произведение с уже введёнными данными")
        print("5 Вывести Лексикографическое произведение с уже введёнными данными")
        print("6 Вывести Дизъюнктивное произведение с уже введёнными данными")
        print("7 Вывести Корневое произведение с уже введёнными данными")
        print("8 Выйти из программы ")
        ans = int(input())

    elif ans == 3:

        T = []
        Tenzor(n, m, T)
        Visualisation(n, m, T)

        print("Выберете цифру, чтобы сделать соответствующее действие")
        print("1 Ввести новые данные")
        print("2 Вывести Декартово произведение с уже введёнными данными")
        print("3 Вывести Тензерное произведение с уже введёнными данными")
        print("4 Вывести Сильное произведение с уже введёнными данными")
        print("5 Вывести Лексикографическое произведение с уже введёнными данными")
        print("6 Вывести Дизъюнктивное произведение с уже введёнными данными")
        print("7 Вывести Корневое произведение с уже введёнными данными")
        print("8 Выйти из программы ")
        ans = int(input())

    elif ans == 4:
        First = []
        Second = []
        Decart(n,m,First)
        Tenzor(n,m,Second)
        i = 0
        k = n*m
        while i < k:
            for _ in Second[i]:
                First[i].append(_)
            i += 1
        Visualisation(n, m, First)

        print("Выберете цифру, чтобы сделать соответствующее действие")
        print("1 Ввести новые данные")
        print("2 Вывести Декартово произведение с уже введёнными данными")
        print("3 Вывести Тензерное произведение с уже введёнными данными")
        print("4 Вывести Сильное произведение с уже введёнными данными")
        print("5 Вывести Лексикографическое произведение с уже введёнными данными")
        print("6 Вывести Дизъюнктивное произведение с уже введёнными данными")
        print("7 Вывести Корневое произведение с уже введёнными данными")
        print("8 Выйти из программы ")
        ans = int(input())

    elif ans == 5:
        L = []
        Leksika(n, m, L)
        Visualisation(n, m, L)

        print("Выберете цифру, чтобы сделать соответствующее действие")
        print("1 Ввести новые данные")
        print("2 Вывести Декартово произведение с уже введёнными данными")
        print("3 Вывести Тензерное произведение с уже введёнными данными")
        print("4 Вывести Сильное произведение с уже введёнными данными")
        print("5 Вывести Лексикографическое произведение с уже введёнными данными")
        print("6 Вывести Дизъюнктивное произведение с уже введёнными данными")
        print("7 Вывести Корневое произведение с уже введёнными данными")
        print("8 Выйти из программы ")
        ans = int(input())

    elif ans == 6:

        D = []
        Diz(n, m, D)
        Visualisation(n, m, D)

        print("Выберете цифру, чтобы сделать соответствующее действие")
        print("1 Ввести новые данные")
        print("2 Вывести Декартово произведение с уже введёнными данными")
        print("3 Вывести Тензерное произведение с уже введёнными данными")
        print("4 Вывести Сильное произведение с уже введёнными данными")
        print("5 Вывести Лексикографическое произведение с уже введёнными данными")
        print("6 Вывести Дизъюнктивное произведение с уже введёнными данными")
        print("7 Вывести Корневое произведение с уже введёнными данными")
        print("8 Выйти из программы ")
        ans = int(input())

    elif ans == 7:
        K = []
        Root(n, m, K)
        Visualisation(n, m, K)

        print("Выберете цифру, чтобы сделать соответствующее действие")
        print("1 Ввести новые данные")
        print("2 Вывести Декартово произведение с уже введёнными данными")
        print("3 Вывести Тензерное произведение с уже введёнными данными")
        print("4 Вывести Сильное произведение с уже введёнными данными")
        print("5 Вывести Лексикографическое произведение с уже введёнными данными")
        print("6 Вывести Дизъюнктивное произведение с уже введёнными данными")
        print("7 Вывести Корневое произведение с уже введёнными данными")
        print("8 Выйти из программы ")
        ans = int(input())
    elif ans == 8:
        v = 0

    else:
        print("Выберете цифру, чтобы сделать соответствующее действие")
        print("1 Ввести новые данные")
        print("2 Вывести Декартово произведение с уже введёнными данными")
        print("3 Вывести Тензерное произведение с уже введёнными данными")
        print("4 Вывести Сильное произведение с уже введёнными данными")
        print("5 Вывести Лексикографическое произведение с уже введёнными данными")
        print("6 Вывести Дизъюнктивное произведение с уже введёнными данными")
        print("7 Вывести Корневое произведение с уже введёнными данными")
        print("8 Выйти из программы ")
        ans = int(input())






# 4
# 3
# 0 1 0 0
# 1 0 1 0
# 0 1 0 1
# 0 0 1 0
# 0 1 0
# 1 0 1
# 0 1 0

# 3
# 4
# 0 1 0
# 1 0 1
# 0 1 0
# 0 1 0 0
# 1 0 1 0
# 0 1 0 1
# 0 0 1 0

# 3
# 4
# 0 0 1
# 0 0 0
# 1 0 0
# 0 0 1 1
# 0 0 0 0
# 1 0 0 0
# 1 0 0 0

# 2
# 3
# 0 1
# 1 0
# 0 0 0
# 0 0 1
# 0 1 0