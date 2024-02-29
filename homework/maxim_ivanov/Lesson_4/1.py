my_dict = {'tuple': (4, 5, 'seven', '10', True), 'list': [True, False, 100, 'null', 'yes'],
           'dict': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'},
           'set': {10, 10, 20, 20, 'last'}}

print(my_dict['tuple'][-1])
my_dict['list'].append('add')
my_dict['list'].pop(1)
my_dict['dict']["'i am a tuple,'"] = 'tuple'
del my_dict['dict']['key5']
my_dict['set'].add(333)
my_dict['set'].pop()
print(my_dict)
