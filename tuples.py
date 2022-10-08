coordinates=(1,2,3)
x,y,z=coordinates
print(x)

values=input('Phone:')
digits_mapping={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four'    
}

output=""
for num in values:
    output += digits_mapping.get(num,'!') + ""
print(output)
