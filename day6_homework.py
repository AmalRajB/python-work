supplies_items=[]

def add_item(item):
    supplies_items.append(item)
    return supplies_items
def count_item(item):
    count=0
    if not item:
        return 0
    else:
        return 1 + count_item(item[1:])

def main():
    # adding items to the list
    add_item("dog_food")
    add_item("cat_toy")
    add_item("bird_cage")
    add_item("fish_tank")
    print(supplies_items)
#   print list usning lamda function
    show_items = lambda item: print(f'item in stock : {item}')
    print('print the list items usning lamda function :')    
    for item in supplies_items:
        show_items(item) 
# print list count using recursion
    print(f'the count of total itmes in the list is : {count_item(supplies_items)}')  

main()       


    
