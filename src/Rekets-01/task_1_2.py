#Даны действительные числа x и y. Получить (|x| − |y|)/(1+ |xy|)

x = float(input(('x = ')))
y = float(input(('y = ')))

z=(abs(x)-abs(y))/(1+abs(x*y))
print('z = ', z)