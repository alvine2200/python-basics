
def swapelements(list, pos1, pos2):
    tmp = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = tmp
    return list


list = [13, 3, 4, 5, 7, 10, 9]
print(list)
pos1 = eval(input('Enter the first position: '))
pos2 = eval(input('Enter the second position: '))


print(swapelements(list, pos1, pos2))
