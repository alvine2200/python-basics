i =1

while i<=5:
    print(i)
    i=i+1
print('done')

secret_number=9
gues_count=0
gues_limit=3
while gues_count < gues_limit:
    gues=int(input('Guess:'))
    gues_count += 1
    if gues ==secret_number:
        print('You win')
        break
else:
    print('Failed, you didnt gues right')
