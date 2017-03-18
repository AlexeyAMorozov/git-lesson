print('Введите координаты вершин треугольника')
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
x3 = int(input('x3: '))
y3 = int(input('y3: '))

a = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
b = ((x3 - x1) ** 2) + ((y3 - y1) ** 2)
c = ((x3 - x2) ** 2) + ((y3 - y2) ** 2)

if (a + b) == c or (a + c) == b or (b + c) == a:
    print('Треугольник прямоугольный!')
else:
    print('Треугольник не прямоугольный!')