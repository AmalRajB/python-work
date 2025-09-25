numof_std=int(input('how many names you want to add : '))
for x in range(numof_std):
    names=input('enter name :')
    
    with open('students.txt','a') as s:

        s.write(names+"\n")
with open('students.txt','r') as s:  
    names = s.read() 
    print(names+'\n')     


    
    


    



    


   
    
    

    


