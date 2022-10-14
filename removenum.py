list1 = [11, 5, 17, 18, 23, 50]

print(list1)


def removenum():
    remove_num = eval(input('Enter the value to remove:'))
    return remove_num


for num in list1:
    if num == removenum():
        list1.remove(num)
        print(list1)
        
