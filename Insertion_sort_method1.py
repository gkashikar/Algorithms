
#Insertion sort involves finding the right place for a given element in a sorted 
#list. So in beginning we compare the first two elements and sort them by comparing
#them. Then we pick the third element and find its proper position among the previous 
#two sorted elements. This way we gradually go on adding more elements to the already 
#sorted list by putting them in their proper position.

# METHOD 1 - INSERTION SORT 

def insertionSort(list1):
    
    # all the values after the first
    index_length = range(1, len(list1))
    
    # to do an operation on all these values
    # for all the value is the index_length value,
    
    for i in index_length:
    
    # we want to sort those values
        sort = list1[i]
    
        # while the item to the left is greater than the item to the right 
        # notice that we also have to write i > 0 bc python allows for negative indexing
        while list1[i-1] > sort and i > 0:
            
            # swap
            list1[i], list1[i-1] = list1[i-1], list1[i]
            
            # to continue doing comparisons down the list,
            # look at the next item
            i = i - 1
 
    return list1

list1 = [7, 3, 4, 1, 9]
insertionSort(list1)
print(list1)

#When the above code is executed, it produces the following result
#[1, 3, 4, 7, 9]
