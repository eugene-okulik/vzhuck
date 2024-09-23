my_dict = {
    'tuple': (1, 5, 10, 'file', 5.55, True), 
    'list': [3, 67, 4, 32, 90], 
    'dict': {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'}, 
    'set': {10, 20, 50, 'qwerty', False, 10, 3, 50}}

                # Для того, что хранится под ключом ‘tuple’:
                #выведите на экран последний элемент
print(my_dict['tuple'][-1])  

                # Для того, что хранится под ключом ‘list’:
                #добавьте в конец списка еще один элемент
my_dict['list'].append(100567) 
print(my_dict['list'])

                # удалите второй элемент списка 
del my_dict['list'][1] 
print(my_dict['list'])

                #Для того, что хранится под ключом ‘dict’:
                # добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict'][('i am a tuple')] = '999999'
print(my_dict['dict'])

                #удалите какой-нибудь элемент
del my_dict['dict'][('two')] 
print(my_dict['dict'])

                #Для того, что хранится под ключом ‘set’:
                #добавьте новый элемент в множество
my_dict['set'].add('new_set_value') 
print(my_dict['set'])

                #удалите элемент из множества
my_dict['set'].remove(False)
print(my_dict['set'])

                # В конце выведите на экран весь словарь
print(my_dict)