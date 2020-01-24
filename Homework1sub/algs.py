import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
   
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
                x[i], x[i+1] = x[i+1], x3[i]
                assign += 2
    print("number of conditionals:", count)
    print("number of assignments:", assign)
                
    return x
    


def quicksort(x):
   
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
   
    def insertionsort(x):
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
  
    

