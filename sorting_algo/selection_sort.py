# This is the list  that i will be testing the algorithm with
mylist = [5,6,8,27,55,2005]  

# n will be used to store the length of the list which will be very important for later
n = len(mylist)
# This for loop will be used to control the second for loop and tell it how many times to run
# So if i wanted to run it 3 times i would use this loop 
for i in range(n-1):
    # This min value will be used to select which index i will be selecting 
    # As the name states selection  
    min_value = i
    for j in range(i+1,n): # The reason this is i+1 is because we comparing second value from i
        # This if statement is used to compare the values 
        if mylist[j]>mylist[min_value]:
            min_value = j  # This changes min because we want to know the position of the min value 
        
        x = mylist.pop(min_value) # This remove the min value form the list 
        mylist.insert(i,x) # This code takes the removed value and inserts it by the compared space

print(mylist) # This is a regular print 