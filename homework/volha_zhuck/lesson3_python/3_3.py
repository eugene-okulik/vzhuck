# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

import math

a = int(input())
b = int(input())
av_ar = (a + b) / 2
av_geo = math.sqrt(a * b)
print(av_ar)
print(av_geo)