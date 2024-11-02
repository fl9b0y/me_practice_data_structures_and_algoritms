# List that needs to be sorted 
mylist = [5,6,8,27,55,2005] 

# Primitive variable used to store length of the list
n = len(mylist)
# This for loop tells the script how many times the inner loop should run
# The reason why its n-1 is because its a bubble sort (also has to do with
# not sorting the last value)
for i in range(n-1):
    swap_bool = False # im using this just so that memory is not wasted if its already sorted
    # Inner loop that actually swaps the values 
    # The reason for the -1 is because we dont want to go above the index of the list
    # The reason for the n-i is because after we finish the first sort there is no need to to look at the last value
    for j in range(n-i-1):
        if mylist[j] < mylist[j+1]:
            mylist[j],mylist[j+1] = mylist[j+1],mylist[j] # simple way of swapping values 
            swap_bool = True
        if not swap_bool: #if its not False then we leave the loop this is so that we dont loop and waste resources
            break
print(mylist)
