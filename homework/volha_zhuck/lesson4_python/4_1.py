my_dict = {
    'tuple': (1, 5, 10, 'file', 5.55, True), 
    'list': [3, 67, 4, 32, 90], 
    'dict': {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'}, 
    'set': {10, 20, 50, 'qwerty', False, 10, 3, 50}}
# Для того, что хранится под ключом ‘tuple’:
print(my_dict['tuple'][-1]) # выведите на экран последний элемент
# Для того, что хранится под ключом ‘list’:
my_dict['list'].append(100567) # добавьте в конец списка еще один элемент
print(my_dict['list'])
del my_dict['list'][1] # удалите второй элемент списка 
print(my_dict['list'])
# Для того, что хранится под ключом ‘dict’:
my_dict['dict']["('i am a tuple',)"] = '999999' # добавьте элемент с ключом ('i am a tuple',) и любым значением
print(my_dict['dict'])
del my_dict['dict'][('two')] # удалите какой-нибудь элемент
print(my_dict['dict'])
# Для того, что хранится под ключом ‘set’:
my_dict['set'].add('new_set_value') # добавьте новый элемент в множество
print(my_dict['set'])
my_dict['set'].remove(False) # удалите элемент из множества
print(my_dict['set'])
print(my_dict) # В конце выведите на экран весь словарь