def addfun(list):
    result = sum(list)
    return result


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sumofnumbers = addfun(list)

distribution = len(list)
average = sumofnumbers/distribution
print(f'Sum of th numbers in the list is: {sumofnumbers}')
print(f'Average of the numbers on the list: {average}')
