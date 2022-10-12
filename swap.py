list = [1, 2, 3, 4, 5, 6, 6, 9]

size = len(list)
first = list[0]
list[0] = list[size-1]
list[size-1] = first
print(list)


def swaplist(mylist):
    mylist[0], mylist[-1] = mylist[-1], mylist[0]
    return mylist


mylist = [2, 3, 4, 5, 6, 6, 9, 10, 6, 98]
print(swaplist(mylist))


# swap at given positions
def swappos(list, pos1, pos2):
    first = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = first
    return list


list = [2, 3, 4, 5, 6, 9, 10, 6, 98]
pos1, pos2 = 1, 2
print(swappos(list, pos1, pos2))


list = [2, 3, 4, 5, 6, 9, 10, 6, 98]
print(len(list))
