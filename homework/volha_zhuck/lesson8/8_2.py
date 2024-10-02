import sys
sys.set_int_max_str_digits(0)

n1 = 5
n2 = 200
n3 = 1000
n4 = 100000
n = [n1, n2, n3, n4]


def fibonachi(limit=1000000):
    a, b = 0, 1
    count = 1
    while count <= limit:
        yield a
        a, b = b, a + b
        count += 1


count = 1
for number in fibonachi(100000):
    if count in n:
        print(number)
    if count > max(n):
        break
    count += 1
