import math

list=[6,2,4,5,6]
list1=[9,3,5,2,3]

print(math.prod(list))
print(math.prod(list1))


def multilist(list):
    result=1
    for num in list:
        result = result*num
    return result


list = [1, 3, 5, 8, 7, 10, 20]
print(multilist(list))
