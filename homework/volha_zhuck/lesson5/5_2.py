s1 = 'результат операции: 42'
s2 = 'результат операции: 514'
s3 = 'результат работы программы: 9'
len1 = len(s1)
len2 = len(s2)
len3 = len(s3)
ind1 = s1.index(':')
ind2 = s2.index(':')
ind3 = s3.index(':')
num1 = int(s1[ind1 + 1:])
num2 = int(s2[ind2 + 1:])
num3 = int(s3[ind3 + 1:])
print(num1 + 10)
print(num2 + 10)
print(num3 + 10)
