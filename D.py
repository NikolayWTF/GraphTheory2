from  tkinter import *
import math

def vizualization (centerX, centerY, radius, angel, X, Y, nm):
    i = 0
    while i < nm:
        x = centerX + radius * math.sin(i * angel)  # Координата новой вершины по x
        y = centerY + radius * math.cos(i * angel)  # И по y
        X.append(x)
        Y.append(y)
        c.create_oval(x, y, x + 10, y + 10, fill="black")  # Рисуем вершину
        c.create_text(x + 15, y - 2, text=f"{i + 1}")  # Подписываем её
        i += 1

root = Tk()
c = Canvas(root, width="2048", heigh="1024") # Создаю окно
c.pack()

c.create_line(0, 350, 1500, 350)
c.create_line(720, 0, 720, 350)

n =  int(input("Введите количество вершин первого графа"))
m =  int(input("Введите количество вершин второго графа"))

centerXn = 360.0
centerYn = 175.0
centerXm = 1080.0
centerYm = 175.0
centerX = 720.0
centerY = 525.0

M = max(n, m)
radiusn = 5*n # Расстояние на которое вершина удалена от центра
radiusm = 5*m
radius = 5*M
angel1 = 2 * math.pi / n # Угол между двумя смежными вершинами
angel2 = 2 * math.pi / m
angel = 2 * math.pi / M
Xn = []
Yn = []
Xm = []
Ym = []
X = []
Y = []
vizualization(centerXn, centerYn, radiusn, angel1, Xn, Yn, n)
vizualization(centerXm, centerYm, radiusm, angel2, Xm, Ym, m)
vizualization(centerX,centerY, radius, angel, X, Y, M)


A = []
i = 0
while i < n:

    a = list(map(int, input(f"Введите {i+1} строчку матрицы смежности для первого графа").split()))
    A.append(a)
    j = 0
    while j < n:
        if (j > i):  # чтобы не рисовать дважды одно ребро, проверяем не было ли оно уже нарисовано
            if (a[j] == 1):
                c.create_line(Xn[i] + 5, Yn[i] + 5, Xn[j] + 5, Yn[j] + 5)  # Создаём рёбра между i-й вершиной и смежными с ней
        j += 1
    i += 1

B = []
i = 0
while i < m:

    b = list(map(int, input(f"Введите {i+1} строчку матрицы смежности для второго графа").split()))
    B.append(b)


    j = 0
    while j < m:
        if (j > i):  # чтобы не рисовать дважды одно ребро, проверяем не было ли оно уже нарисовано
            if (b[j] == 1):
                c.create_line(Xm[i] + 5, Ym[i] + 5, Xm[j] + 5, Ym[j] + 5)  # Создаём рёбра между i-й вершиной и смежными с ней
        j += 1
    i += 1

C = []
i = 0

minimum = min(m, n)
if minimum == n:
    while i < minimum:
        j = 0
        while j < minimum:
            B[i][j] += A[i][j]
            if (B[i][j] == 2):
                B[i][j] = 1

            j += 1
        i += 1

    i = 0
    while i < M:
        j = 0
        while j < M:
            if (B[i][j] == 1):
                c.create_line(X[i] + 5, Y[i] + 5, X[j] + 5, Y[j] + 5)  # Создаём рёбра между i-й вершиной и смежными с ней
            j += 1
        i += 1

else:
    while i < minimum:
        j = 0
        while j < minimum:
            A[i][j] += B[i][j]
            if (A[i][j] == 2):
                A[i][j] = 1
            if (A[i][j] == 1):
                c.create_line(X[i] + 5, Y[i] + 5, X[j] + 5, Y[j] + 5)  # Создаём рёбра между i-й вершиной и смежными с ней

            j += 1
        i += 1
    i = 0
    while i < M:
        j = 0
        while j < M:
            if (A[i][j] == 1):
                c.create_line(X[i] + 5, Y[i] + 5, X[j] + 5,
                              Y[j] + 5)  # Создаём рёбра между i-й вершиной и смежными с ней
            j += 1
        i += 1




root.mainloop()

# 3
# 4
# 0 1 0
# 1 0 1
# 0 1 0
# 0 0 0 1
# 0 0 1 0
# 0 1 0 1
# 1 0 1 0


# 5
# 4
# 0 1 0 0 1
# 1 0 1 0 1
# 0 1 0 1 1
# 0 0 1 0 1
# 1 1 1 1 0
# 0 0 1 1
# 0 0 0 1
# 1 0 0 0
# 1 1 0 0


