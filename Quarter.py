print('Введите координаты X:')
x = int(input())
print('Введите координаты Y:')
y = int(input())

def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    elif x == 0:
        return 'Точка на оси X'
    elif y == 0:
        return 'Точка на оси Y'

print('Точка принадлежит четверти: {}'.format(quarter(x, y)))