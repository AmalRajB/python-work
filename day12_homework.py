import re
name=input('enter your name : ')
feedback=input('give  a feedback :')

try:
    if name=='':
        raise ValueError('name field is required')
    if feedback=='':
        raise ValueError('feedback field is required')
    if not re.fullmatch(r'^[A-Za-z ]+',name):
        raise ValueError('please enter a valid name')
    if not re.fullmatch(r'^[A-Za-z0-9\s]{5,100}',feedback):
        raise ValueError('your feedback must contain atleast 8 characters and ')
    print(f'{name} thankyou for sharing your details.....')

except ValueError as ve:
    print(ve)
finally:
    print('task ended...')        
