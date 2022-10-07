for x in range(4):
    for y in range(4):
        print(f"({x},{y})")
        
numbers=[5,2,5,2,2] 
#for number in numbers:
#   print("X" * number)

for number in numbers:
    output=""
    for count in range(number):
        output += 'x'
    print(output)
     
