#Вычислить квадратное уравнение
# ax2 + bx + c = 0 (*)
#D = b2 – 4ac;
#x1,2 = (-b +/- sqrt (D)) / 2a
#Предусмотреть 3 варианта:
#1) Два действительных корня
#2) Один действительный корень
#3) Нет действительных корней

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

D = b ** 2 - 4 * a * c
print("D =", D)

x_1 = (-b + pow(((b ** 2 - 4 * a * c)), 1 / 2)) / 2 * a
x_2 = (-b - pow(((b ** 2 - 4 * a * c)), 1 / 2)) / 2 * a
x_0 = -b / 2 * a

if D > 0:
    print(x_1, x_2)
if D == 0:
    print(x_0)
if D < 0:
    print('error')
