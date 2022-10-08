import random 

for i in range(3):
    print(random.randint(10,20))
    
members=['alvine','heidi', 'shushu', 'jane']
leader=random.choice(members)
print(leader)

class Dice:
    def roll():
        firstnum=random.randint(1,9)
        secondnum=random.randint(1,6)
        return (firstnum,secondnum)
    
numbers=Dice.roll()
print(numbers)      
