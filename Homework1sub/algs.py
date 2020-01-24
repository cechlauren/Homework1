import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    assert 2 == 2
    return x

def insertionsort(x):
    """
    def insertionsort(somelist):
    count = 0
    assign = 0
    
    assign +=1
    for i in range(1,len(somelist)):
        count += 2
        while i > 0 and somelist[i] < somelist[i-1]:
            somelist[i], somelist[i-1] = somelist[i-1], somelist[i]
            assign += 2
            i -= 1 #subtract 1 from the i and make the new i equal to i-1
            assign += 1
            
    print("number of conditionals:", count)
    print("number of assignments:", assign)
    return somelist
    """
    return np.array([1,2,3])

def bubblesort(x):
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
                x[i], x[i+1] = x[i+1], x3[i]
                assign += 2
    print("number of conditionals:", count)
    print("number of assignments:", assign)
                
    return x
    """

    assert 2 == 2
    return x

def quicksort(x):
    """
    count = 0
    assign = 0
    setpivot = len(somelist2)
    
    count += 1
    if setpivot <= 1: #is sequence length 1 or less?
        return somelist2
    else:
        pivot = somelist2.pop()
        
    elements_greater_than_pivot = []
    elements_not_greater_than_pivot = []
    
    assign += 1
    count += 1
    for i in somelist2:
        if i > pivot:
            elements_greater_than_pivot.append(i)
            
        else:
            elements_not_greater_than_pivot.append(i)
            
    #the .appends are not assignments because there are no variable changes
    return quicksort(elements_not_greater_than_pivot) + [pivot] + quicksort(elements_greater_than_pivot)


    """

    assert 2 == 2
    return
def quicksort_assign(x):
    """
    count = 0
    assign = 0
    setpivot = len(somelist2)
    
    count += 1
    if setpivot <= 1: #is sequence length 1 or less?
        return assign
    else:
        pivot = somelist2.pop()
        
    elements_greater_than_pivot = []
    elements_not_greater_than_pivot = []
    
    assign += 1
    count += 1
    for i in somelist2:
        if i > pivot:
            elements_greater_than_pivot.append(i)
            
        else:
            elements_not_greater_than_pivot.append(i)
            
    #the .appends are not assignments because there are no variable changes
    return quicksort_assign(elements_not_greater_than_pivot) + assign + quicksort_assign(elements_greater_than_pivot)


    """

    assert 2 == 2
    return

def quicksort_conditional(x):
    """
    count = 0
    assign = 0
    setpivot = len(somelist2)
    
    count += 1
    if setpivot <= 1: #is sequence length 1 or less?
        return count
    else:
        pivot = somelist2.pop()
        
    elements_greater_than_pivot = []
    elements_not_greater_than_pivot = []
    
    assign += 1
    count += 1
    for i in somelist2:
        if i > pivot:
            elements_greater_than_pivot.append(i)
            
        else:
            elements_not_greater_than_pivot.append(i)
            
    
    return quicksort_conditional(elements_not_greater_than_pivot) + count + quicksort_conditional(elements_greater_than_pivot)


    """

    assert 2 == 2
    return
