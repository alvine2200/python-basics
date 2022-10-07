# if name < 3 char, name must be atleast 3 characters
# otherwise if its > 50 char, name can be a maximum of 50char
# otherwise name looks good

name = input('Enter name: ')

if len(name) < 3:
    print('name must be atleast 3 characters')
elif len(name) > 50:
    print('name can be a maximum of 50 characers')
else:
    print('name looks good')
