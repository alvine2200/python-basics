from more_itertools import first


first='Alvine'
last='Llavu'

message=first+' ['+last+'] is a coder' 

#formatted string
you=f'{first} [{last}] is a coder '
result=you.upper()
lower=you.lower()
print(result)
print(lower)
print(you )
print(len(you))
me=message.replace('Alvine','Absolute Beginners')
him=message.find('A')
print(him)
print(me)