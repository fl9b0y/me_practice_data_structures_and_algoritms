mylist = [5,4,8,27,55,2005,7,66] 
n = len(mylist)
for i in range(1,n):
    insert_index = i
    current_value = mylist.pop(i)
    for j in range(i-1,-1,-1):
        if mylist[j] > current_value:
            current_index = j
    mylist.insert(current_index,current_value)
print(mylist)