import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
   """
   more detailed explanations in my jupyter file but:
   #bubblesort pseudocode
#define function bubblesort(takes unsorted sequence, list_a):
    #make an indexing length of where we are going to make comparisons
    #indexing_length = len(list_a) - 1 #because cant do a comparison on the last number in the list due to the fact that there's no number after it
    #make a local variable that we use in the function
    #sorted = False #use this sorted variable within our control flow to break us out once its been sorted
    
    #do iterations 
    #while not sorted (ie while that variable is false) we do the following actions:
        #reference sorted = True
        
        #for i in range(0, indexing_length) want to do comparison:
            #if list_a[i] (value to left) > list_a[i+1] (value to right):
                #sorted = False (not sorted so need to fix)
                #list_a[i], list_a[i+1] = list_a[i+1], list_a[i] (flips the positions of those values)
                
            #once all items are sorted, the if statement wont activate, so the sorted variable remains true which allows us to break out of the while loop

#return list_a
#print the sorted list bubblesort([9,8,7,6,9,8,7,6,1])
   """
    count = 0
    assign = 0
    index_length = len(x)-1
    sorted = False #escape while loop
    
    count += 1
    while not sorted: #repeat until sorted = True
        sorted = True
        
       
        for i in range(0, index_length):
            assign += 1
            
            count += 1
            if x[i] > x[i+1]:
                
                sorted = False #values are not sorted
                x[i], x[i+1] = x[i+1], x[i]
                assign += 2
    print("number of conditionals:", count)
    print("number of assignments:", assign)
                
    return x
    


def quicksort(x):
    
    """
    #Quicksort pseudocode:
#define function as quicksort(takes some unsorted sequence): #apply it to the first sequence that we pass in and subsequent subsequences that we create
#only apply the function to the sequence if they have a length > 1
    #length = len(sequence)
        #if length <= 1:
            #return the sequence (allows us to skip seq that have a length of one or zero)
        #for everything else:
            #(define our pivot) pivot = sequence.pop()  #removes our last element and also returns it
            #need to create two lists that we can move an item to once its compared to our pivot point
            
        #new list for items greater and smaller than pivot 
        #items_greater = []
        #items_lower = []
        
        #now do a comparison on each of the items left in our sequence to the pivot point
        #for item in sequence:
            #if item > pivot:
                #append that item to the greater list
                #items_greater.append(item)
                
            #else(item<=pivot):
                #items_lower.append(item)
        #apply this over and over to each of the sublists that we create, using a return statement
        #return quicksort(items_lower) + concatenate pivot point in center of sequence [pivot] + quicksort(items_greater)
        
        #print(quicksort([list]))
    
    """
   
    count = 0
    assign = 0
    setpivot = len(x)
    
    count += 1
    if setpivot <= 1: #is sequence length 1 or less?
        return x
    else:
        pivot = x.pop()
        
    elements_greater_than_pivot = []
    elements_not_greater_than_pivot = []
    
    assign += 1
    count += 1
    for i in x:
        if i > pivot:
            elements_greater_than_pivot.append(i)
            
        else:
            elements_not_greater_than_pivot.append(i)
            
    #the .appends are not assignments because there are no variable changes
    return quicksort(elements_not_greater_than_pivot) + [pivot] + quicksort(elements_greater_than_pivot)


def insertionsort(x):
    
    
    """"
    #Insertionsort psuedocode:
#definition insertion_sort(takes a list of values called list_a):
    #indexing_length = range(start at 1, end at length(list_a)) #in sorting algorithm the first element is already "sorted" 
#(now do an operation on all those values after the first element in the sequence!)
    #for i in the indexing_length values: #(start sorting values)
        #variable name: value_to_sort = list_a[at i position] #goes one by one in the "unsorted" indexing length so we can sort them
        
        #(create a while loop that lets us look for conditions when the value to the left is larger than the value we're trying to sort
        #while (the item to immediate left in our list) list_a[i-1] > value_to_sort and i>0 (bc dont want to get to neg indices)
            #(write the switch code)
            #list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            #(continue doing comparisons down the list)
            #(i is now equal to i-1) i = i-1
            
    #(exit the loop so that we can return sorted list_a)
    #return list_a
    
#print(insertion_sort([takes unsorted list in comma separated values]))
    
    """"
   
    count = 0
    assign = 0
    
    assign +=1
    for i in range(1,len(x)):
        count += 2
        while i > 0 and x[i] < x[i-1]:
            x[i], x[i-1] = x[i-1], x[i]
            assign += 2
            i -= 1 #subtract 1 from the i and make the new i equal to i-1
            assign += 1
            
    print("number of conditionals:", count)
    print("number of assignments:", assign)
    return x
  
    

