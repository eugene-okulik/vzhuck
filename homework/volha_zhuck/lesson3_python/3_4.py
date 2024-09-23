# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
import math

a = int(input())
b = int(input())
c = math.sqrt(a**2 + b**2)
s = 0.5 * a * b
print(c)
print(s)