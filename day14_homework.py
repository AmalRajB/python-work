import random
import math

customes=input('enter the customers name (comma-separated) : ')
cust_name=customes.split(',')
names=list(set(cust_name))
# finalres=random.shuffle(names)
x=random.choices(names, k=2)
reversed_list=[s[::-1] for s in x]
squareroot=math.sqrt(len(names))
print(f'winners name : {reversed_list}')
print(f'the total number of unique participants : {len(names)}')
print(f'the square root of the number of participants : {round(squareroot)}')


