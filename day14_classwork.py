import random
import math
names=input('enter the names : ')
x=names.split(',')
result=list(set(x))
# print(result)
revresult=random.choice(result)
def revfn(s):
    str=''
    for x in s:
        str=x+str
    return str    
print(f'the randomly choosen name is : {revfn(revresult)}')
print(f'the total number of unique names is : {len(result)}')
sr=math.sqrt(len(result))
finalsr=math.ceil(sr)
print(f'the rounded square root of total number is : {finalsr}' )






