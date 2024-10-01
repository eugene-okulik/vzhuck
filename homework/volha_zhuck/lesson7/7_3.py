s1 = 'результат операции: 42'
s2 = 'результат операции: 514'
s3 = 'результат работы программы: 9'
s4 = 'результат: 2'
list = [s1, s2, s3, s4]

def plus10(s):
    ind = s.index(':')
    num = int(s[ind + 1:])
    result = num + 10
    print(result)

def getnums(list):
    for str in list:
        plus10(str)
        
getnums(list)
