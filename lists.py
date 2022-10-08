names=['john','Alvine','Jane','Mosh','Bob']
print(names[1:])

#largest number in a list
numbers=[1,0,3,4,9,30,0,45,2,34,34,43]
max=numbers[0]
for number in numbers:
    if number > max:
        max=number
print(max)

uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)