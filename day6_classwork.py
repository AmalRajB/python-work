Grocery_List = ["milk","bread","eggs"]
def add_item(item):
    Grocery_List.insert(0, item)
    Grocery_List.pop()
    return Grocery_List
add_item("butter")
print(Grocery_List)

list = lambda x : print(f'item : {x}')
for x in Grocery_List:
    list(x)

def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])
print(count_characters(Grocery_List)) 
    
   
    


      
