count = 0
total = 0

attendance = [18, 20, 19, 15, 21]
for day in attendance:
    if day >= 20:
        print(f'The {day} is full')
        count = count+1
    else:
        print(f'the {day} not full')
    total += day  
print(f'count of classes that full: {count}')
print(f'the total attendance for all 5 days : {total}')


