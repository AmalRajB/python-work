import os

item=input('enter the item name : ')
if os.path.exists('item.txt'):
    f=open('item.txt','a')
    f.write(f'{item}\n')
    f.close
else:
    f=open('item.txt','w')
    f.write(f'{item}\n')
    f.close()

f=open('item.txt','r')
print(f.read())  
f.close()  

