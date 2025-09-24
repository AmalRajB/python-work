import re

input1=input('enter the book title : ')
input2= input('enter publication year : ')

try:
    txt=input1
    txt2=input2
    if not re.fullmatch(r'^[A-Za-z ]+',txt):
        raise ValueError('the book title only contain alphabets and space')
    if not re.fullmatch(r'^(19|20)\d{2}',txt2):
        raise ValueError('the publish year start with 19 or 20 and must have 4 digits')
    print('book accepted...')
except ValueError as vr:
    print(vr)
finally:
    print('operation ended....')    
           


