import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x): #define function bubblesort(takes unsorted sequence, list_a):

    count = 0
    assign = 0
    index_length = len(x)-1 #make an indexing length of where we are going to make comparisons
    #indexing_length = len(list_a) - 1 #because cant do a comparison on the last number in the list due to the fact that there's no number after it
    sorted = False #use this sorted variable within our control flow to break us out once its been sorted
    
    count += 1
    #do iterations 
    while not sorted: #while not "sorted=False" we do the following actions:
        sorted = True
        
       
        for i in range(0, index_length): #for i in range(0, indexing_length) want to do comparison:
            assign += 1
            
            count += 1
            if x[i] > x[i+1]: #if x[i] (value to left) > x[i+1] (value to right):
                
                sorted = False #sorted = False bc not sorted so need to fix
                x[i], x[i+1] = x[i+1], x[i] # (flips the positions of those values)
                assign += 2
    #once all items are sorted, the if statement wont activate, so the sorted variable remains true which allows us to break out of the while loop
    print("number of conditionals:", count)
    print("number of assignments:", assign)
                
    return x
    


def quicksort(x): #define function as quicksort(takes some unsorted sequence): #apply it to the first sequence that we pass in and subsequent subsequences that we create
    
    count = 0
    assign = 0
    setpivot = len(x)
    
    count += 1
    if setpivot <= 1:  #only apply the function to the sequence if they have a length > 1
        return x  #return the sequence (allows us to skip seq that have a length of one or zero)
    else: #for everything else:
        pivot = x.pop()  #(define our pivot) pivot = sequence.pop()  #removes our last element and also returns it
        
    #need to create two lists that we can move an item to once its compared to our pivot point
    #new list for items greater and smaller than pivot 
    elements_greater_than_pivot = []
    elements_not_greater_than_pivot = []
    
    assign += 1
    count += 1
    for i in x: #for item in sequence:
        if i > pivot:  #now do a comparison on each of the items left in our sequence to the pivot point
            elements_greater_than_pivot.append(i)  #append that item to the greater list
            
        else: #else(item<=pivot):
            elements_not_greater_than_pivot.append(i)
            
    #apply this over and over to each of the sublists that we create, using a return statement
    #the .appends are not assignments because there are no variable changes
    return quicksort(elements_not_greater_than_pivot) + [pivot] + quicksort(elements_greater_than_pivot)
    #return quicksort(items_lower) + concatenate pivot point in center of sequence [pivot] + quicksort(items_greater)


def insertionsort(x):
    
  #definition insertion_sort(takes a list of values called list_a):  
   
    count = 0
    assign = 0
    
    assign +=1
    for i in range(1,len(x)): #indexing_length = range(start at 1, end at length(list_a)) #in sorting algorithm the first element is already "sorted" 
         #(now do an operation on all those values after the first element in the sequence!)
        count += 2
        while i > 0 and x[i] < x[i-1]:    #(create a while loop that lets us look for conditions when the value to the left is larger than the value we're trying to sort
            x[i], x[i-1] = x[i-1], x[i] #(write the switch code)
            assign += 2
            #(continue doing comparisons down the list)
            i -= 1 #subtract 1 from the i and make the new i equal to i-1
            assign += 1
            
    print("number of conditionals:", count)
    print("number of assignments:", assign)
    return x
  
    

